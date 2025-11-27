% rebase('layout.tpl', title='Nova Conta')

<section class="form-section">
    <h1>Nova Conta Bancária</h1>

    <form action="{{action}}" method="post" class="form-container">
        <div class="form-group">
            <label for="numero">Número da Conta:</label>
            <input type="number" id="numero" name="numero" required placeholder="Ex: 1001">
        </div>

        <div class="form-group">
            <label for="titular">Nome do Titular:</label>
            <input type="text" id="titular" name="titular" required placeholder="Ex: João Silva">
        </div>

        <div class="form-group">
            <label for="saldo">Saldo Inicial (R$):</label>
            <input type="number" step="0.01" id="saldo" name="saldo" value="0.00">
        </div>

        <div class="form-actions">
            <button type="submit" class="btn-submit">Salvar Conta</button>
            <a href="/conta" class="btn-cancel">Voltar</a>
        </div>
    </form>
</section>