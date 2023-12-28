from covabra import Covabra
from datetime import date, timedelta

# Objetos Covabra
covabra_cic = Covabra()
covabra_cic.banco_connection("CIC")
covabra_cic.banco_engine()

covabra_venda = Covabra()
covabra_venda.banco_connection("VENDA")
covabra_venda.banco_engine()

def main():
    # Variáveis de Tempo
    data_atual = date.today()
    data_passada = date.today().replace(day=1) - timedelta(days=1)
    particao_atual = str(data_atual.year) + str(data_atual.month)
    particao_passada = str(data_passada.year) + str(data_passada.month)

    # DataFrame Room
    sat_series = covabra_venda.banco_query(caminho_sql="sql/sat_series.sql", params={"particao_atual": particao_atual, "particao_passada": particao_passada})
    sat_series.rename(columns={"loja": "Loja", "pdv": "PDV", "data_ultima_venda": "Data da Última Venda"}, inplace=True)
    sat_series.to_excel(r"content/PDVs_SAT.xlsx", index=False)

    if len(sat_series) > 0:
        covabra_cic.email_enviar(titulo="PDVs Inativos (SAT) - Fiscal", email_html="email_fiscal.html",  destinatarios_tag=(173, "A"), anexos=["content/PDVs_SAT.xlsx"])

if __name__ == "__main__":
    main()