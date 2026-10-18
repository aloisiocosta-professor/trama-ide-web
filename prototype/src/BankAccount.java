import java.math.BigDecimal;
import java.util.Objects;

// Exemplo didatico: valores decimais, nao um sistema bancario de producao.
public final class BankAccount {
    // @begin balance
    private BigDecimal balance;
    // @end balance

    // @begin constructor
    public BankAccount(BigDecimal initial) {
        Objects.requireNonNull(initial, "Valor inicial obrigatorio");
        if (initial.signum() < 0) throw new IllegalArgumentException("Saldo inicial negativo");
        balance = initial;
    }
    // @end constructor

    // @begin deposit
    public void deposit(BigDecimal amount) {
        positive(amount);
        balance = balance.add(amount);
    }
    // @end deposit

    // @begin withdraw
    public void withdraw(BigDecimal amount) {
        positive(amount);
        if (amount.compareTo(balance) > 0) throw new IllegalArgumentException("Saldo insuficiente");
        balance = balance.subtract(amount);
    }
    // @end withdraw

    // @begin getBalance
    public BigDecimal getBalance() {
        return balance;
    }
    // @end getBalance

    private static void positive(BigDecimal amount) {
        Objects.requireNonNull(amount, "Valor obrigatorio");
        if (amount.signum() <= 0) throw new IllegalArgumentException("Valor deve ser positivo");
    }
}
