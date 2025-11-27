% rebase('layout.tpl', title=f'{tipo.capitalize()} - Conta {numero}')

<section class="form-section">
    <h1>{{tipo.capitalize()}} na Conta {{numero}}</h1>

    <form action="/conta/{{tipo}}/{{numero}}" method="post" class="form-container">
        <div class="form-group">
            <label for="valor">Valor (R$):</label>
            <input type="number" step="0.01" id="valor" name="valor" required placeholder="0.00">
        </div>

        <div class="form-actions">
            <button type="submit" class="btn-submit">Confirmar {{tipo.capitalize()}}</button>
            <a href="/conta" class="btn-cancel">Cancelar</a>
        </div>
    </form>
</section>