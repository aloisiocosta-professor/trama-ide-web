import copy
import json
import unittest
from pathlib import Path
from generate import generate

class GeneratorChecks(unittest.TestCase):
    def setUp(self): self.model=json.loads(Path(__file__).with_name('model.json').read_text())
    def test_structural_contract(self):
        source=generate(self.model)
        self.assertIn('private BigDecimal balance;',source)
        self.assertIn('public void deposit(BigDecimal amount)',source)
        self.assertIn('UnsupportedOperationException',source)
    def test_rejects_code_in_identifier(self):
        self.model['class']='X; arbitrary'
        with self.assertRaises(ValueError):generate(self.model)
    def test_rejects_duplicate_attribute(self):
        self.model['attributes']*=2
        with self.assertRaises(ValueError):generate(self.model)
    def test_rejects_void_parameter(self):
        self.model['constructor'][0]['type']='void'
        with self.assertRaises(ValueError):generate(self.model)
    def test_rejects_duplicate_parameter(self):
        self.model['constructor']*=2
        with self.assertRaises(ValueError):generate(self.model)

if __name__=='__main__':unittest.main()
