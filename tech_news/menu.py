import sys

from tech_news.analyzer.ratings import top_5_categories, top_5_news
from tech_news.analyzer.search_engine import (search_by_category,
                                              search_by_date, search_by_tag,
                                              search_by_title)
from tech_news.scraper import get_tech_news


# Requisito 12
def analyzer_menu():
    selected_option = input(
        "Selecione uma das opções a seguir:\n"
        " 0 - Popular o banco com notícias;\n"
        " 1 - Buscar notícias por título;\n"
        " 2 - Buscar notícias por data;\n"
        " 3 - Buscar notícias por tag;\n"
        " 4 - Buscar notícias por categoria;\n"
        " 5 - Listar top 5 notícias;\n"
        " 6 - Listar top 5 categorias;\n"
        " 7 - Sair."
    )

    queries = {
        "0": "Digite quantas notícias serão buscadas:",
        "1": "Digite o título:",
        "2": "Digite a data no formato aaaa-mm-dd:",
        "3": "Digite a tag:",
        "4": "Digite a categoria:",
    }

    functions = {
        "0": get_tech_news,
        "1": search_by_title,
        "2": search_by_date,
        "3": search_by_tag,
        "4": search_by_category,
        "5": top_5_news,
        "6": top_5_categories,
    }

    if selected_option in ["0", "1", "2", "3", "4"]:
        value = input(queries[selected_option])
        print(functions[selected_option](value))
    elif selected_option in ["5", "6"]:
        print(functions[selected_option]())
    elif selected_option == "7":
        print("Encerrando script")
    else:
        sys.stderr.write("Opção inválida\n")
