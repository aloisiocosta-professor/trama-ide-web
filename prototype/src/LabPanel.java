import java.awt.*;
import java.math.BigDecimal;
import java.util.ArrayList;
import java.util.List;
import javax.swing.*;
import javax.swing.text.DefaultHighlighter;

/** Interface experimental: o parametro visual nao muda o executor Java. */
public final class LabPanel extends JPanel {
    private final TraceEngine engine = new TraceEngine();
    private final SourceMap sourceMap;
    private final boolean linked;
    private final JTextArea source = new JTextArea();
    private final JTextArea state = new JTextArea();
    private final JTextArea history = new JTextArea();
    private final JLabel explanation = new JLabel("Crie duas contas e escolha uma operacao.");
    private final JComboBox<String> targets = new JComboBox<>();
    private final JTextField name = new JTextField("contaAna", 10);
    private final JTextField amount = new JTextField("100.00", 8);
    private final JTextField prediction = new JTextField(25);
    private final JTextField justification = new JTextField(25);
    private final List<String> localResponses = new ArrayList<>();
    private final java.util.Map<String,JButton> umlButtons = new java.util.LinkedHashMap<>();

    public LabPanel(String actualSource, boolean linked) {
        this.linked = linked;
        this.sourceMap = new SourceMap(actualSource);
        name.setName("reference-name"); amount.setName("amount"); targets.setName("target");
        prediction.setName("prediction"); justification.setName("explanation");
        setLayout(new BorderLayout(12, 12));
        setBorder(BorderFactory.createEmptyBorder(16, 16, 16, 16));
        setBackground(new Color(244, 247, 251));
        JLabel title = new JLabel("UML · codigo · objetos Java", SwingConstants.LEFT);
        title.setFont(new Font(Font.SANS_SERIF, Font.BOLD, 25));
        title.setBorder(BorderFactory.createEmptyBorder(0,0,12,0));
        add(title, BorderLayout.NORTH);
        JPanel center = new JPanel(new GridLayout(1,3,12,0));
        JPanel uml = new JPanel(); uml.setLayout(new BoxLayout(uml,BoxLayout.Y_AXIS));
        uml.add(new JLabel("BankAccount"));
        for (String[] member : new String[][]{
            {"balance", "- balance: BigDecimal"}, {"constructor", "+ BankAccount(initial)"},
            {"deposit", "+ deposit(amount): void"}, {"withdraw", "+ withdraw(amount): void"},
            {"getBalance", "+ getBalance(): BigDecimal"}}) {
            JButton button = new JButton(member[1]);
            button.setAlignmentX(Component.LEFT_ALIGNMENT);
            button.addActionListener(e -> select(member[0]));
            umlButtons.put(member[0], button); uml.add(button); uml.add(Box.createVerticalStrut(8));
        }
        JTextArea description = new JTextArea("Uma classe define o tipo.\nCada objeto tem seu estado.\nDuas referencias podem apontar\npara o mesmo objeto.");
        description.setEditable(false); description.setLineWrap(true); description.setWrapStyleWord(true);
        uml.add(description);
        center.add(card("1 · Classe UML (subconjunto)", uml));
        source.setText(actualSource); source.setEditable(false); source.setFont(new Font(Font.MONOSPACED,Font.PLAIN,12));
        center.add(card("2 · Fonte Java compilado", new JScrollPane(source)));
        JPanel runtime = new JPanel(new GridLayout(2,1,0,8));
        state.setEditable(false); history.setEditable(false);
        state.setFont(new Font(Font.MONOSPACED,Font.PLAIN,13));
        runtime.add(new JScrollPane(state)); runtime.add(new JScrollPane(history));
        center.add(card("3 · Referencias, objetos e chamadas", runtime));
        add(center,BorderLayout.CENTER);
        JPanel bottom = new JPanel(); bottom.setLayout(new BoxLayout(bottom,BoxLayout.Y_AXIS));
        JPanel controls = new JPanel(new FlowLayout(FlowLayout.LEFT));
        controls.add(new JLabel("Nome/alias:")); controls.add(name);
        controls.add(new JLabel("Valor:")); controls.add(amount);
        JButton create = new JButton("Criar conta"); create.addActionListener(e -> perform(() -> engine.create(name.getText().trim(), value()))); controls.add(create);
        controls.add(new JLabel("Referencia:")); controls.add(targets);
        JButton alias = new JButton("Criar alias"); alias.addActionListener(e -> perform(() -> engine.alias(name.getText().trim(), target()))); controls.add(alias);
        for(String key:new String[]{"deposit","withdraw","getBalance"}) {
            JButton call = new JButton(key); call.addActionListener(e -> perform(() -> engine.invoke(target(),key,key.equals("getBalance")?null:value()))); controls.add(call);
        }
        bottom.add(controls);
        JPanel responses = new JPanel(new FlowLayout(FlowLayout.LEFT));
        responses.add(new JLabel("Previsao:")); responses.add(prediction);
        responses.add(new JLabel("Explicacao:")); responses.add(justification);
        JButton savePrediction = new JButton("Guardar previsao");
        savePrediction.addActionListener(e -> recordPrediction(prediction.getText()));
        JButton saveExplanation = new JButton("Guardar explicacao");
        saveExplanation.addActionListener(e -> recordExplanation(justification.getText()));
        responses.add(savePrediction); responses.add(saveExplanation); bottom.add(responses);
        explanation.setBorder(BorderFactory.createEmptyBorder(8,0,8,0)); bottom.add(explanation);
        JButton export = new JButton("Exportar sessao local (TSV)");
        export.addActionListener(e -> export()); bottom.add(export);
        bottom.add(new JLabel("Prototipo de pesquisa · respostas locais · nao mede aprendizagem automaticamente"));
        add(bottom, BorderLayout.SOUTH); updateState(null);
    }
    private JPanel card(String title, Component content) {
        JPanel panel=new JPanel(new BorderLayout(0,8));
        panel.setBorder(BorderFactory.createCompoundBorder(BorderFactory.createLineBorder(new Color(210,218,230)),BorderFactory.createEmptyBorder(12,12,12,12)));
        JLabel label=new JLabel(title); label.setFont(new Font(Font.SANS_SERIF,Font.BOLD,14)); panel.add(label,BorderLayout.NORTH); panel.add(content,BorderLayout.CENTER);return panel;
    }
    private BigDecimal value() { return new BigDecimal(amount.getText().trim()); }
    private String target() { if(targets.getSelectedItem()==null)throw new IllegalArgumentException("Crie uma conta primeiro");return targets.getSelectedItem().toString(); }
    private void select(String key) {
        source.getHighlighter().removeAllHighlights();
        umlButtons.values().forEach(b -> b.setBackground(null));
        if (!linked) { explanation.setText("Elemento selecionado. Consulte o fonte e os objetos."); return; }
        SourceMap.Region region=sourceMap.region(key);
        try { source.getHighlighter().addHighlight(region.startOffset(),region.endOffset(),new DefaultHighlighter.DefaultHighlightPainter(new Color(255,231,135)));source.setCaretPosition(region.startOffset()); }
        catch(javax.swing.text.BadLocationException e){ throw new IllegalStateException(e); }
        umlButtons.get(key).setBackground(new Color(255,231,135));
        explanation.setText("Correspondencia: UML "+key+" -> fonte, linhas "+region.firstLine()+" a "+region.lastLine()+" -> estado do objeto receptor.");
    }
    private void perform(java.util.function.Supplier<TraceEngine.Event> operation) {
        try { accept(operation.get()); }
        catch(RuntimeException error) { explanation.setText("Operacao rejeitada: "+error.getMessage()); }
    }
    public void accept(TraceEngine.Event event) {
        if(event.member().equals("alias")) {
            source.getHighlighter().removeAllHighlights();
            umlButtons.values().forEach(b -> b.setBackground(null));
            explanation.setText("Alias: duas referencias para a mesma identidade. A atribuicao ocorre fora de BankAccount.");
        } else select(event.member());
        updateState(event);
    }
    private void updateState(TraceEngine.Event event) {
        String selected=(String)targets.getSelectedItem();targets.removeAllItems();
        StringBuilder text=new StringBuilder("REFERENCIA -> IDENTIDADE -> SALDO\n\n");
        engine.snapshot().forEach((key,value)->{ targets.addItem(key);text.append(key).append(" -> ").append(value.objectId()).append(" -> ").append(value.balance());if(linked&&event!=null&&event.changed().contains(key))text.append("  [ALTERADO]");text.append('\n'); });
        if(selected!=null)targets.setSelectedItem(selected);
        if(event!=null){ text.append("\nANTES: ").append(event.before()).append("\nDEPOIS: ").append(event.after()); }
        state.setText(text.toString());
        StringBuilder calls=new StringBuilder("HISTORICO DE CHAMADAS\n");
        for(TraceEngine.Event item:engine.events()) {
            if(item.member().equals("alias"))calls.append(item.target()).append(" = ").append(item.argument()).append('\n');
            else calls.append(item.target()).append('.').append(item.member()).append('(').append(item.argument()).append(")\n");
        }
        history.setText(calls.toString());
    }
    private static String clean(String value){return value.replace('\t',' ').replace('\n',' ').replace('\r',' ');}
    private void export() {
        JFileChooser chooser=new JFileChooser(); chooser.setSelectedFile(new java.io.File("sessao-local.tsv"));
        if(chooser.showSaveDialog(this)!=JFileChooser.APPROVE_OPTION)return;
        java.nio.file.Path path=chooser.getSelectedFile().toPath();
        if(java.nio.file.Files.exists(path)&&JOptionPane.showConfirmDialog(this,"Substituir arquivo existente?","Exportar",JOptionPane.YES_NO_OPTION)!=JOptionPane.YES_OPTION)return;
        StringBuilder data=new StringBuilder("tipo\tconteudo\n");
        for(String response:localResponses)data.append("resposta\t").append(clean(response)).append('\n');
        for(TraceEngine.Event event:engine.events())data.append("evento\t").append(clean(event.toString())).append('\n');
        try{ java.nio.file.Files.writeString(path,data.toString(),java.nio.charset.StandardCharsets.UTF_8);explanation.setText("Sessao exportada localmente."); }
        catch(java.io.IOException error){explanation.setText("Falha ao exportar: "+error.getMessage());}
    }
    public TraceEngine engine(){return engine;}
    public void recordPrediction(String text){recordResponse("previsao",text);}
    public void recordExplanation(String text){recordResponse("explicacao",text);}
    private void recordResponse(String kind,String text){
        localResponses.add(kind+" | eventos="+engine.events().size()+" | "+text);
        explanation.setText("Resposta guardada somente nesta sessao local: "+localResponses.size());
    }
    public List<String> responses(){return List.copyOf(localResponses);}
    public boolean linked(){return linked;}
    public int highlightedRegions(){return source.getHighlighter().getHighlights().length;}
}
