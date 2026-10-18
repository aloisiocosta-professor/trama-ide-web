import java.util.LinkedHashMap;
import java.util.Map;

/** Mapeamento explicito: comentarios delimitam trechos do fonte efetivamente exibido. */
public final class SourceMap {
    public record Region(int firstLine, int lastLine, int startOffset, int endOffset) {}
    private final Map<String, Region> regions = new LinkedHashMap<>();

    public SourceMap(String source) {
        String[] lines = source.split("\n", -1);
        Map<String, Integer> starts = new LinkedHashMap<>();
        Map<String, Integer> offsets = new LinkedHashMap<>();
        int offset = 0;
        for (int i = 0; i < lines.length; i++) {
            String line = lines[i].trim();
            if (line.startsWith("// @begin ")) {
                String key = line.substring(10).trim();
                if (starts.containsKey(key) || regions.containsKey(key)) throw new IllegalArgumentException("Marcador duplicado: " + key);
                starts.put(key, i + 2);
                offsets.put(key, offset + lines[i].length() + 1);
            } else if (line.startsWith("// @end ")) {
                String key = line.substring(8).trim();
                Integer first = starts.remove(key);
                Integer start = offsets.remove(key);
                if (first == null || i + 1 <= first) throw new IllegalArgumentException("Marcador sem inicio/trecho: " + key);
                regions.put(key, new Region(first, i, start, offset));
            }
            offset += lines[i].length() + 1;
        }
        if (!starts.isEmpty()) throw new IllegalArgumentException("Trecho sem fim");
        for (String key : new String[]{"balance", "constructor", "deposit", "withdraw", "getBalance"}) region(key);
    }

    public Region region(String key) {
        Region region = regions.get(key);
        if (region == null) throw new IllegalArgumentException("Trecho nao mapeado: " + key);
        return region;
    }
}
