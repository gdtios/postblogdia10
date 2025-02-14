from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Post
from .forms import PostForm

def lista_posts(request):
    posts = Post.objects.all().order_by('-data_publicacao')
    return render(request, 'meus_posts/lista_posts.html', {'posts': posts})

@login_required
def criar_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.autor = request.user
            post.save()
            return redirect('lista_posts')
    else:
        form = PostForm()
    return render(request, 'meus_posts/form_post.html', {'form': form})


def blank_page(request):
    return render(request, 'blank_page.html')

from .service_rag import rag_function_perplexity

def minha_view_rag_perplexity(request): # Nome da view atualizado
    if request.method == 'POST':
        user_query = request.POST.get('user_query')
        # documentos_fonte = [
        #     "Documento 1: ... conteúdo do documento 1 ...",
        #     "Documento 2: ... conteúdo do documento 2 ...",
        #     "Documento 3: ... conteúdo do documento 3 ..."
        # ]
        documentos_fonte = [
            "Python é uma linguagem de programação de alto nível, interpretada, de propósito geral e muito popular.",
            "Uma das características do Python é a sua legibilidade, o que significa que o código Python é fácil de ler e entender.",
            "Tipos de dados básicos em Python incluem inteiros (int), números de ponto flutuante (float), strings (str) e booleanos (bool).",
            "Listas em Python são coleções ordenadas e mutáveis de itens, escritas com colchetes [].",
            "Tuplas são coleções ordenadas e imutáveis de itens, escritas com parênteses ().",
            "Dicionários em Python são coleções não ordenadas, mutáveis e indexadas de itens, escritos com chaves {}.",
            "Estruturas de controle de fluxo em Python incluem 'if', 'elif', 'else' para decisões e 'for' e 'while' para loops.",
            "Funções em Python são blocos de código reutilizáveis definidos com a palavra-chave 'def'.",
            "Módulos em Python são arquivos contendo definições e declarações Python. Você pode importar módulos para reutilizar código.",
            "O tratamento de exceções em Python é feito com blocos 'try', 'except', 'finally' para lidar com erros de forma elegante.",
            "Python suporta programação orientada a objetos (POO) com classes e objetos.",
            "Virtual environments em Python são usados para criar ambientes isolados para projetos, gerenciando dependências separadamente.",
            "Pip é o gerenciador de pacotes padrão para Python, usado para instalar e gerenciar bibliotecas e dependências.",
            "F-strings em Python (a partir da versão 3.6) são uma forma concisa e legível de formatar strings, usando f'...'."
        ]
        perplexity_api_key = "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" # **Configure sua chave API aqui (ou melhor, em variáveis de ambiente)**

        resposta = rag_function_perplexity(user_query, documentos_fonte, perplexity_api_key) # Chama a função RAG da Perplexity

        return render(request, 'meus_posts/template_da_sua_view.html', {'pergunta': user_query, 'resposta_rag': resposta})

    return render(request, 'meus_posts/template_da_sua_view.html')
