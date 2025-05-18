import os
from google.colab import userdata
from google.genai import types
from google import genai
import ipywidgets as widgets
from IPython.display import display

def setup():
  os.environ['GOOGLE_API_KEY'] = userdata.get('GOOGLE_API_KEY')
  source = get_source()
  instructions = get_instructions(source)


# --- Função para Montar as instruções ---
def get_instructions(sampleData):
    template_instructions = f"""
    Você é um assistente especialista em detecção de fraudes e golpes online no Brasil.
    Sua tarefa é analisar o texto fornecido pelo usuário e identificar possíveis sinais de fraude.
    Considere os seguintes indicadores comuns de golpes (mas não se limite a eles):

    1.  **Senso de Urgência:** Frases como "somente hoje", "última chance", "sua conta será bloqueada".
    2.  **Erros de Português e Gramática:** Textos mal escritos, com erros grosseiros.
    3.  **Links Suspeitos:** URLs encurtadas de forma estranha, domínios que não correspondem à empresa oficial, ou que pedem para clicar imediatamente.
    4.  **Solicitação de Dados Pessoais ou Bancários:** Pedidos de senhas, números de cartão de crédito, CPF, códigos de segurança, tokens. Nenhuma instituição séria pede isso por mensagem ou e-mail não solicitado.
    5.  **Ofertas Boas Demais para Serem Verdade:** Prêmios inesperados, empréstimos com condições irreais, produtos muito baratos.
    6.  **Tom Ameaçador ou Intimidador:** Ameaças de multas, processos judiciais, ou consequências negativas se não houver uma ação imediata.
    7.  **Remetente Desconhecido ou Suspeito:** Endereços de e-mail estranhos, números de telefone não familiares se passando por empresas.
    8.  **Pedido de Pagamento Antecipado para Liberar Algo Maior:** Taxas para liberar prêmios, empréstimos, etc.
    9.  **Inconsistências:** Informações que não batem com o que você sabe sobre a suposta empresa ou pessoa.
    10. **Formas de Pagamento Incomuns:** Pedidos de transferência para contas de pessoa física, pagamento via Pix para chaves aleatórias ou CPFs desconhecidos em nome de empresas.

    Considere também a cartilha abaixo com os golpes mais comuns relatados:
    CARTILHA:
    ---
    {sampleData}
    ---
    ANÁLISE:
    Com base no texto fornecido verifique se o relato se parece com algum golpe relatado na cartilha.
    Se for, use as orientações da cartilha.
    Senão, identifique os possíveis indicadores de fraude e indique por que são suspeitos.
    Forneça uma recomendação geral ao usuário (ex: "Cuidado, pode ser um golpe. Não clique em links nem forneça dados."
    ou "Parece legítimo, mas verifique o remetente.").

    Seja claro, objetivo e útil. Forneça um resumo dos pontos de atenção.
    """

    chat_config = types.GenerateContentConfig(
      system_instruction = template_instructions
    )

    return chat_config

def formatador(message):
  model = "models/gemini-2.0-flash"
  chat_config = types.GenerateContentConfig(
      system_instruction = "Você formata textos em HTML."
  )
  return get_gemini_answer(chat_config, message)

# --- Obtem a resposta do Gemini usando as instruções e um prompt ---

def get_gemini_answer(instructions, user_prompt):
    model = "models/gemini-2.0-flash"
    try:
        client = genai.Client()
        chat = client.chats.create(model=model, config=instructions)
        response = chat.send_message(user_prompt)
        return response.text
    except Exception as e:
        return f"Ocorreu um erro ao gerar a resposta: {e}"

# --- Lê um arquivo de um caminho parametrizado ---

def read_file(file_path):
  if __name__ == "__main__":
    source = extract_text_from_txt(file_path)

    if source:
        return source
    else:
        return "No Content"

# --- Lê e retorna o conteúdo da cartilha ---

def get_source():
  file_path = "/content/sample_data/cartilha-golpe-2025.txt"
  return read_file(file_path)


# --- Análise do Relato com as Instruções
def ask_gemini(prompt):
  answer = get_gemini_answer(instructions, prompt)
  relato_usuario = textarea.value
  #Exemplo Verdadeiro -> Positivo: Telefonema dizendo que meu sobrinho se acidentou
  #Exemplo Verdadeiro -> Negativo: Recebi o SMS: O Ministério da Saúde convida: vacine-se contra a gripe no Dia D.
  resposta = get_gemini_answer(instructions, relato_usuario)
  return resposta


# --- Front End Components ---

# Create textarea widgets
def create_textarea():
    return widgets.Textarea(
      value='',
      placeholder='Relate uma situação que você desconfia...',
      description='',
      layout=widgets.Layout(width='50%', height='100px')
    )

# Create a button widget
def create_button():
  button = widgets.Button(
      description='Analisar Fraude',
      button_style='success'
  )
  button.on_click(on_button_click)
  return button

# Create main label
def create_label():
  return widgets.HTML()

def display_ui():
  display(textarea)
  display(button)
  display(response_label)

def feedback(text):
  response_label.value = text

# Set click event
def on_button_click(b):
    feedback("Analisando...")
    response = ask_gemini(textarea.value)
    formatted_response = formatador(response)
    feedback(formatted_response)

# -- UI ---
textarea = create_textarea()
button = create_button()
response_label = create_label()

# -- Main --
setup()
display_ui()
