import java.awt.*;
import java.awt.image.BufferedImage;
import java.math.BigDecimal;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.Map;
import javax.imageio.ImageIO;
import javax.swing.SwingUtilities;

/** Verificacao tecnica deterministica, sem participantes ou resultados educacionais. */
public final class LabChecks {
    private static int checks=0;
    private static void check(boolean ok,String label){checks++;if(!ok)throw new AssertionError(label);System.out.println("PASS "+label);}
    private static BigDecimal value(String s){return new BigDecimal(s);}
    private static void rejects(Runnable action,String label){boolean rejected=false;try{action.run();}catch(IllegalArgumentException|NullPointerException e){rejected=true;}check(rejected,label);}
    private static void layout(Container container){container.doLayout();for(Component child:container.getComponents())if(child instanceof Container nested)layout(nested);}
    private static void render(LabPanel panel,Path path)throws Exception{
        panel.setSize(1450,850);layout(panel);
        BufferedImage image=new BufferedImage(1450,850,BufferedImage.TYPE_INT_RGB);
        Graphics2D graphics=image.createGraphics();panel.printAll(graphics);graphics.dispose();
        ImageIO.write(image,"png",path.toFile());
        check(Files.size(path)>10000,"offscreen render "+path.getFileName());
    }
    public static void main(String[] args)throws Exception{
        Path output=Path.of(args[1]);Files.createDirectories(output);
        String source=Files.readString(Path.of(args[0]));SourceMap mapping=new SourceMap(source);
        check(source.substring(mapping.region("deposit").startOffset(),mapping.region("deposit").endOffset()).contains("balance = balance.add(amount)"),"source mapping deposit");
        rejects(()->new SourceMap(source.replace("// @end deposit","// @end other")),"broken source mapping rejected");
        TraceEngine e=new TraceEngine();
        e.create("ana",value("0.00"));e.create("bruno",value("7.50"));
        check(!e.snapshot().get("ana").objectId().equals(e.snapshot().get("bruno").objectId()),"distinct instances");
        TraceEngine.Event deposit=e.invoke("ana","deposit",value("0.10"));
        e.invoke("ana","deposit",value("0.20"));
        check(e.snapshot().get("ana").balance().equals("0.30"),"decimal exactness");
        check(e.snapshot().get("bruno").balance().equals("7.50"),"other instance unchanged");
        check(deposit.before().get("ana").balance().equals("0.00"),"before snapshot immutable");
        check(deposit.after().get("ana").balance().equals("0.10"),"after snapshot immutable");
        check(deposit.changed().equals(java.util.Set.of("ana")),"changed receiver");
        e.alias("aliasAna","ana");e.invoke("aliasAna","deposit",value("1.00"));
        check(e.snapshot().get("ana").objectId().equals(e.snapshot().get("aliasAna").objectId()),"alias identity");
        check(e.snapshot().get("ana").balance().equals("1.30"),"alias changes same object");
        check(e.events().get(e.events().size()-1).changed().equals(java.util.Set.of("ana","aliasAna")),"both references reflect change");
        e.invoke("ana","withdraw",value("0.30"));
        check(e.snapshot().get("ana").balance().equals("1.00"),"withdrawal actual Java");
        Map<String,TraceEngine.State> before=e.snapshot();int n=e.events().size();
        rejects(()->e.invoke("ana","withdraw",value("100")),"insufficient funds");
        rejects(()->e.invoke("ana","deposit",value("0")),"zero deposit");
        rejects(()->e.invoke("ana","deposit",value("-1")),"negative deposit");
        rejects(()->e.create("ana",value("2")),"duplicate name");
        rejects(()->e.create("bad name",value("2")),"invalid name");
        rejects(()->e.create("negative",value("-2")),"negative initial state");
        rejects(()->e.invoke("missing","deposit",value("2")),"unknown reference");
        rejects(()->e.invoke("ana","unknown",value("2")),"unknown operation");
        check(before.equals(e.snapshot())&&n==e.events().size(),"rejected calls preserve state and successful history");
        e.invoke("ana","getBalance",null);check(before.equals(e.snapshot()),"getter does not mutate");
        final Exception[] failure={null};
        SwingUtilities.invokeAndWait(()->{
            try{
                LabPanel linked=new LabPanel(source,true),plain=new LabPanel(source,false);
                for(LabPanel panel:new LabPanel[]{linked,plain}){
                    panel.accept(panel.engine().create("ana",value("100.00")));
                    panel.accept(panel.engine().create("bruno",value("20.00")));
                    panel.recordPrediction("Apenas ana vai mudar");
                    panel.accept(panel.engine().invoke("ana","deposit",value("25.00")));
                    panel.recordExplanation("O receptor e ana");
                }
                check(linked.engine().snapshot().equals(plain.engine().snapshot()),"A/B equal semantic states");
                check(linked.engine().events().equals(plain.engine().events()),"A/B equal semantic traces");
                check(linked.highlightedRegions()==1&&plain.highlightedRegions()==0,"A/B visual intervention differs");
                check(linked.responses().get(0).contains("eventos=2")&&linked.responses().get(1).contains("eventos=3"),"response chronology preserved");
                render(linked,output.resolve("linked.png"));render(plain,output.resolve("plain.png"));
            }catch(Exception ex){failure[0]=ex;}
        });
        if(failure[0]!=null)throw failure[0];
        String result="{\"status\":\"pass\",\"checks\":"+checks+",\"educational_participants\":0,\"scope\":\"deterministic technical validation only\"}\n";
        Files.writeString(output.resolve("technical-results.json"),result);
        System.out.println(result);
    }
}
