import unittest
from research_governance import validate_inventory,conventional,assess_completion

def entry(path):return {'path':path,'sha256':'a'*64}

class GovernanceChecks(unittest.TestCase):
    def test_template_is_governed(self):
        with self.assertRaisesRegex(ValueError,'missing'):
            validate_inventory(['.github/pull_request_template.md'],[])
    def test_new_artifact_cannot_be_omitted(self):
        with self.assertRaisesRegex(ValueError,'new.md'):
            validate_inventory(['docs/research/old.md','docs/session/new.md'],[entry('docs/research/old.md')])
    def test_product_files_are_outside_research_manifest(self):
        self.assertEqual(validate_inventory(['app.js','docs/research/a.md'],[entry('docs/research/a.md')]),1)
    def test_duplicate_path_is_rejected(self):
        with self.assertRaisesRegex(ValueError,'Duplicate'):
            validate_inventory(['AGENTS.md'],[entry('AGENTS.md')]*2)
    def test_deleted_artifact_cannot_stay_listed(self):
        with self.assertRaisesRegex(ValueError,'extra'):
            validate_inventory([],[entry('paper/deleted.md')])
    def test_invalid_hash_rejected(self):
        with self.assertRaisesRegex(ValueError,'SHA'):
            validate_inventory(['AGENTS.md'],[{'path':'AGENTS.md','sha256':'wrong'}])
    def test_conventional_examples(self):
        self.assertTrue(conventional('docs(research): add evidence (#1)'))
        self.assertFalse(conventional('update stuff'))
    def test_closed_not_planned_is_not_complete(self):
        root={'number':1,'state':'closed','state_reason':'completed'}
        child={'number':2,'state':'closed','state_reason':'not_planned'}
        self.assertEqual(assess_completion(root,[child],[2])['status'],'incomplete')
    def test_missing_child_is_not_complete(self):
        root={'number':1,'state':'closed','state_reason':'completed'}
        self.assertEqual(assess_completion(root,[],[2])['status'],'incomplete')
    def test_parent_must_be_completed(self):
        root={'number':1,'state':'open','state_reason':None}
        child={'number':2,'state':'closed','state_reason':'completed'}
        self.assertEqual(assess_completion(root,[child],[2])['status'],'incomplete')
    def test_all_completed(self):
        root={'number':1,'state':'closed','state_reason':'completed'}
        child={'number':2,'state':'closed','state_reason':'completed'}
        self.assertEqual(assess_completion(root,[child],[2])['status'],'complete')

if __name__=='__main__':unittest.main()
