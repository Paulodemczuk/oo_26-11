% rebase('layout.tpl', title='Gestão de Contas')

<section class="users-section"> <h1>Contas Bancárias</h1>
    
    <a href="/conta/criar" class="btn btn-primary" style="margin-bottom: 20px; display: inline-block;">
        Nova Conta
    </a>

    <table class="styled-table" border="1" style="width: 100%; border-collapse: collapse;">
        <thead>
            <tr>
                <th>Número</th>
                <th>Titular</th>
                <th>Saldo (R$)</th>
                <th>Ações</th>
            </tr>
        </thead>
        <tbody>
            % for c in contas:
            <tr>
                <td>{{c.numero}}</td>
                <td>{{c.titular}}</td>
                <td>R$ {{'{:.2f}'.format(c.saldo)}}</td>
                <td>
                    <a href="/conta/depositar/{{c.numero}}" class="btn-small" style="color: green;">[+] Depositar</a>
                    <a href="/conta/sacar/{{c.numero}}" class="btn-small" style="color: red;">[-] Sacar</a>
                </td>
            </tr>
            % end
        </tbody>
    </table>
</section>