"""
Transcrição de áudio para texto usando Google Speech Recognition
Converte arquivos de áudio .wav em texto
"""

import speech_recognition as sr
import os


def transcrever_audio(arquivo_audio, arquivo_saida):
    """Transcreve áudio para texto e salva em arquivo"""
    reconhecedor = sr.Recognizer()
    
    with sr.AudioFile(arquivo_audio) as source:
        audio = reconhecedor.record(source)
        
        try:
            # Usar Google Speech Recognition em português
            texto = reconhecedor.recognize_google(audio, language="pt-BR")
            print(f"Transcrição: {texto}")
            
            # Salvar em arquivo
            with open(arquivo_saida, 'w', encoding='utf-8') as f:
                f.write(texto)
            
            return texto
            
        except sr.UnknownValueError:
            print("Não foi possível entender o áudio")
            return None
        except sr.RequestError as e:
            print(f"Erro ao acessar serviço: {e}")
            return None


def main():
    """Função principal"""
    diretorio = os.path.dirname(os.path.abspath(__file__))
    arquivo_audio = os.path.join(diretorio, 'audio1.wav')
    arquivo_texto = os.path.join(diretorio, 'transcricao_audio.txt')

    transcrever_audio(arquivo_audio, arquivo_texto)


if __name__ == "__main__":
    main()

