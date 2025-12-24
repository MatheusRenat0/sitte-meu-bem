from flask import Flask, render_template, jsonify, send_from_directory
import os

app = Flask(__name__)

timeline_data = [
    {
        "year": "Janeiro",
        "title": "Começando Juntos",
        "description": "Obrigado por estar ao meu lado desde o início deste ano. Sua presença faz cada dia valer a pena.",
        "image": "foto1.jpg",
        "easter_egg": "Você faz tudo melhor! 💛"
    },
    {
        "year": "Fevereiro",
        "title": "Cumplicidade",
        "description": "Agradeço por cada risada compartilhada, cada conversa até tarde da noite. Você é minha melhor companhia.",
        "image": "foto2.jpg",
        "easter_egg": "Minha pessoa favorita! 😍"
    },
    {
        "year": "Março",
        "title": "Nos Desafios",
        "description": "Obrigado por estar comigo nos momentos difíceis. Sua força e apoio me fizeram superar tudo.",
        "image": "foto3.jpg",
        "easter_egg": "Juntos somos mais fortes! 💪"
    },
    {
        "year": "Abril",
        "title": "Pequenos Momentos",
        "description": "Agradeço pelos detalhes: seu sorriso ao acordar, seu abraço apertado, suas mensagens de bom dia.",
        "image": "foto4.jpg",
        "easter_egg": "Os detalhes fazem a diferença! ⭐"
    },
    {
        "year": "Maio",
        "title": "Aventuras Juntos",
        "description": "Obrigado por topar cada ideia maluca, cada passeio, cada aventura. Ao seu lado tudo é diversão.",
        "image": "foto5.jpg",
        "easter_egg": "Nossos rolês são os melhores! ✈️"
    },
    {
        "year": "Junho",
        "title": "Seu Apoio",
        "description": "Agradeço por acreditar em mim quando nem eu acreditava. Você é minha maior incentivadora.",
        "image": "foto6.jpg",
        "easter_egg": "Você me faz crescer! 🎉"
    },
    {
        "year": "Julho",
        "title": "Nosso Refúgio",
        "description": "Obrigado por ser meu porto seguro. Com você, qualquer lugar parece lar.",
        "image": "foto7.jpg",
        "easter_egg": "Meu lugar favorito é com você! 💕"
    },
    {
        "year": "Agosto",
        "title": "Paciência e Amor",
        "description": "Agradeço por sua paciência com meus defeitos e por me amar mesmo quando eu não sou perfeito.",
        "image": "foto8.jpg",
        "easter_egg": "Amor que aceita e acolhe! 🏡"
    },
    {
        "year": "Setembro",
        "title": "Crescendo Juntos",
        "description": "Obrigado por crescer comigo, por construir sonhos juntos. Nossa parceria é tudo para mim.",
        "image": "foto9.jpg",
        "easter_egg": "Time perfeito! 💑"
    },
    {
        "year": "Dezembro",
        "title": "Gratidão Eterna",
        "description": "Chegamos ao final do ano e meu coração transborda de gratidão. Obrigado por cada segundo ao meu lado.",
        "image": "foto10.jpg",
        "easter_egg": "Para sempre grato por você! 🎂"
    }
]

achievements = [
    {
        "icon": "🤝",
        "title": "Companheirismo Verdadeiro",
        "description": "Você esteve ao meu lado em absolutamente tudo este ano. Nos bons momentos e nos desafios, sempre juntos."
    },
    {
        "icon": "💪",
        "title": "Minha Fortaleza",
        "description": "Sua força me inspira todos os dias. Quando eu fraquejo, você me levanta. Somos um time imbatível."
    },
    {
        "icon": "❤️",
        "title": "Amor Incondicional",
        "description": "Agradeço por me amar do jeito que sou, com defeitos e qualidades. Seu amor me transforma."
    },
    {
        "icon": "✨",
        "title": "Luz nos Meus Dias",
        "description": "Você ilumina até os dias mais cinzas. Sua energia positiva é contagiante e transformadora."
    },
    {
        "icon": "🎯",
        "title": "Parceira de Sonhos",
        "description": "Obrigado por sonhar comigo, por planejar nosso futuro, por acreditar no que podemos construir juntos."
    },
    {
        "icon": "🌟",
        "title": "Pessoa Extraordinária",
        "description": "Inteligente, engraçada, carinhosa e única. Ter você na minha vida é meu maior presente."
    }
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/timeline')
def get_timeline():
    return jsonify(timeline_data)

@app.route('/api/achievements')
def get_achievements():
    return jsonify(achievements)

@app.route('/static/<path:path>')
def send_static(path):
    return send_from_directory('static', path)

if __name__ == '__main__':
    # Criar pastas necessárias se não existirem
    os.makedirs('static/images', exist_ok=True)
    os.makedirs('static/music', exist_ok=True)
    os.makedirs('templates', exist_ok=True)
    
    print("=" * 50)
    print("💝 SITE DE AGRADECIMENTO - PRONTO PARA USAR! 💝")
    print("=" * 50)
    print("\n📁 ESTRUTURA DE PASTAS:")
    print("   ├── app.py (este arquivo)")
    print("   ├── templates/")
    print("   │   └── index.html")
    print("   └── static/")
    print("       ├── images/")
    print("       │   ├── foto1.jpg até foto10.jpg")
    print("       └── music/")
    print("           └── song.mp3")
    print("\n📸 ADICIONE SUAS 10 FOTOS em: static/images/")
    print("   Nomeie como: foto1.jpg, foto2.jpg ... foto10.jpg")
    print("   Sugestão: use fotos dos meses correspondentes!")
    print("\n🎵 ADICIONE SUA MÚSICA em: static/music/song.mp3")
    print("\n🚀 Servidor rodando em: http://localhost:5000")
    print("=" * 50)
    print()
    
    app.run(debug=True)