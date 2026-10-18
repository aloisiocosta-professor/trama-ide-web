import java.math.BigDecimal;
import java.util.ArrayList;
import java.util.Collections;
import java.util.IdentityHashMap;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Map;
import java.util.Objects;
import java.util.Set;
import java.util.LinkedHashSet;

/** Executor unico para ambas as condicoes visuais. Nenhuma simulacao JavaScript. */
public final class TraceEngine {
    public record State(String objectId, String balance) {}
    public record Event(String target, String member, String argument,
                        Map<String, State> before, Map<String, State> after, Set<String> changed) {}
    private final Map<String, BankAccount> references = new LinkedHashMap<>();
    private final IdentityHashMap<BankAccount, String> identities = new IdentityHashMap<>();
    private final List<Event> events = new ArrayList<>();
    private int nextId = 1;

    private static void name(String name) {
        if (name == null || !name.matches("[A-Za-z][A-Za-z0-9_]{0,19}")) throw new IllegalArgumentException("Nome invalido");
    }
    private void unused(String name) {
        name(name);
        if (references.containsKey(name)) throw new IllegalArgumentException("Nome ja usado");
    }
    private BankAccount account(String name) {
        BankAccount value = references.get(name);
        if (value == null) throw new IllegalArgumentException("Referencia inexistente");
        return value;
    }
    public synchronized Map<String, State> snapshot() {
        Map<String, State> state = new LinkedHashMap<>();
        references.forEach((key, value) -> state.put(key, new State(identities.get(value), value.getBalance().toPlainString())));
        return Collections.unmodifiableMap(state);
    }
    private Event record(String target, String member, String argument, Map<String, State> before) {
        Map<String, State> after = snapshot();
        Set<String> changed = new LinkedHashSet<>();
        after.forEach((key, value) -> { if (!Objects.equals(before.get(key), value)) changed.add(key); });
        Event event = new Event(target, member, argument, before, after, Collections.unmodifiableSet(changed));
        events.add(event);
        return event;
    }
    public synchronized Event create(String name, BigDecimal initial) {
        unused(name);
        Map<String, State> before = snapshot();
        BankAccount object = new BankAccount(initial);
        identities.put(object, "obj" + nextId++);
        references.put(name, object);
        return record(name, "constructor", initial.toPlainString(), before);
    }
    public synchronized Event alias(String newName, String existing) {
        unused(newName);
        BankAccount object = account(existing);
        Map<String, State> before = snapshot();
        references.put(newName, object);
        return record(newName, "alias", existing, before);
    }
    public synchronized Event invoke(String target, String member, BigDecimal amount) {
        BankAccount object = account(target);
        Map<String, State> before = snapshot();
        switch (member) {
            case "deposit" -> object.deposit(amount);
            case "withdraw" -> object.withdraw(amount);
            case "getBalance" -> object.getBalance();
            default -> throw new IllegalArgumentException("Metodo fora do subconjunto");
        }
        return record(target, member, amount == null ? "" : amount.toPlainString(), before);
    }
    public synchronized List<Event> events() { return List.copyOf(events); }
}
