import java.nio.file.Files;
import java.nio.file.Path;
import javax.swing.*;

public final class LabApp {
    public static void main(String[] args) throws Exception {
        if(args.length<1)throw new IllegalArgumentException("Informe caminho de BankAccount.java [linked|plain]");
        String source=Files.readString(Path.of(args[0]));
        boolean linked=args.length<2||args[1].equals("linked");
        if(args.length>1&&!args[1].equals("linked")&&!args[1].equals("plain"))throw new IllegalArgumentException("Condicao deve ser linked ou plain");
        SwingUtilities.invokeLater(()->{
            JFrame frame=new JFrame("Laboratorio UML e objetos Java");
            frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
            frame.setContentPane(new LabPanel(source,linked));
            frame.setSize(1450,850);frame.setLocationRelativeTo(null);frame.setVisible(true);
        });
    }
}
