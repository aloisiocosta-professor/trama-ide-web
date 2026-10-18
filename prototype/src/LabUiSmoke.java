import java.awt.*;
import java.awt.image.BufferedImage;
import java.math.BigDecimal;
import java.nio.file.Files;
import java.nio.file.Path;
import javax.imageio.ImageIO;
import javax.swing.*;

/** Ensaio funcional em display Xvfb; nao envolve usuarios ou mede usabilidade. */
public final class LabUiSmoke {
    private static JFrame frame;
    private static LabPanel panel;
    private static int checks=0;
    private static void check(boolean value,String label){checks++;if(!value)throw new AssertionError(label);System.out.println("PASS UI "+label);}
    private static Component named(Container root,String name){
        for(Component child:root.getComponents()){
            if(name.equals(child.getName()))return child;
            if(child instanceof Container nested){Component found=named(nested,name);if(found!=null)return found;}
        }
        return null;
    }
    private static JButton button(Container root,String text){
        for(Component child:root.getComponents()){
            if(child instanceof JButton b&&text.equals(b.getText()))return b;
            if(child instanceof Container nested){JButton found=button(nested,text);if(found!=null)return found;}
        }
        return null;
    }
    private static JFileChooser chooser(Container root){
        for(Component child:root.getComponents()){
            if(child instanceof JFileChooser c)return c;
            if(child instanceof Container nested){JFileChooser found=chooser(nested);if(found!=null)return found;}
        }
        return null;
    }
    private static void field(String name,String text){((JTextField)named(panel,name)).setText(text);}
    private static void click(String text){JButton b=button(panel,text);if(b==null)throw new AssertionError("Botao ausente: "+text);b.doClick();}
    public static void main(String[] args)throws Exception{
        Path source=Path.of(args[0]),output=Path.of(args[1]);Files.createDirectories(output);
        String code=Files.readString(source);
        try{
            SwingUtilities.invokeAndWait(()->{
                frame=new JFrame("Ensaio tecnico local");panel=new LabPanel(code,true);
                frame.setContentPane(panel);frame.setSize(1450,850);frame.setLocation(0,0);frame.setVisible(true);
                check(frame.isShowing(),"visible frame");
                field("reference-name","ana");field("amount","100.00");click("Criar conta");
                field("reference-name","bruno");field("amount","20.00");click("Criar conta");
                check(panel.engine().snapshot().size()==2,"creation through buttons");
                ((JComboBox<?>)named(panel,"target")).setSelectedItem("ana");
                field("prediction","Apenas ana muda");click("Guardar previsao");
                field("amount","25.00");click("deposit");
                check(panel.engine().snapshot().get("ana").balance().equals("125.00"),"deposit through button");
                check(panel.engine().snapshot().get("bruno").balance().equals("20.00"),"other instance preserved");
                field("explanation","A chamada tem receptor ana");click("Guardar explicacao");
                check(panel.responses().size()==2,"responses through buttons");
            });
            Path target=output.resolve("ui-session.tsv").toAbsolutePath();
            Files.deleteIfExists(target);
            SwingUtilities.invokeAndWait(()->{
                Timer approve=new Timer(150,null);
                approve.addActionListener(e->{
                    for(Window window:Window.getWindows()){
                        if(!window.isShowing())continue;
                        JFileChooser selection=chooser(window);
                        if(selection!=null){selection.setSelectedFile(target.toFile());selection.approveSelection();approve.stop();return;}
                    }
                });
                approve.start();click("Exportar sessao local (TSV)");approve.stop();
            });
            check(Files.exists(target),"file chooser export");
            String exported=Files.readString(target);
            check(exported.contains("previsao | eventos=2")&&exported.contains("explicacao | eventos=3")&&exported.contains("deposit"),"exported chronology and event");
            Robot robot=new Robot();robot.waitForIdle();
            BufferedImage screenshot=robot.createScreenCapture(frame.getBounds());
            ImageIO.write(screenshot,"png",output.resolve("ui-smoke.png").toFile());
            Files.writeString(output.resolve("ui-smoke-results.json"),"{\"status\":\"pass\",\"checks\":"+checks+",\"human_participants\":0,\"scope\":\"automated displayed Swing workflow\"}\n");
        }finally{if(frame!=null)SwingUtilities.invokeAndWait(()->frame.dispose());}
    }
}
