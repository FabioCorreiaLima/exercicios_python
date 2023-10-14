import pygame
pygame.init()
pygame.mixer.music.lood(music.mp3) # aqui irá o arquivo mp3
pygame.event.wait()





def gravar():
    arquivo = open(nomeArquivo,'a')
    arquivo.write('Nome.....:%s' % vnome.get())
    arquivo.write('Telefone.....:%s' % vtelefone.get())
    arquivo.write('Nª/Apartamento.....:%s' % vapart.get())
    arquivo.write('\n\n')


