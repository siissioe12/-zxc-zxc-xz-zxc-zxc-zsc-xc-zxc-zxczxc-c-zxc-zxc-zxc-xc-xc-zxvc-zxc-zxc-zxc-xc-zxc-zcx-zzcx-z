import pygame
import sys

# Marco, usa i commenti.
# Se usiamo i commenti ci capiamo meglio
# Ah, le variabili (se ne metti) dagli nomi che hanno senso e sono umani (Es. Variabile che definisce i soldi che ho in banca = soldi). 
# Non chiamarla (la variabile) code tipo "<sdfgaernadrbaefnaetbalfivnsfdvuaysdbvuyafbauhvilbhadufbe7rhgvihalelvhulnvHILFHn" Ok?

# Inizializza Pygame
pygame.init()

# Imposta le dimensioni della finestra
larghezza, altezza = 1920, 1080

# Crea la finestra
finestra = pygame.display.set_mode((larghezza, altezza), pygame.RESIZABLE)

# Imposta il titolo della finestra
pygame.display.set_caption("ROTFL")

# Stato iniziale a schermo intero
fullscreen = False

# Loop principale
while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            # Chiudi la finestra e esci dal programma
            pygame.quit()
            sys.exit()
        elif evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_F6:
                # Cambia a schermo intero o finestra
                fullscreen = not fullscreen
                if fullscreen:
                    pygame.display.set_mode((larghezza, altezza), pygame.FULLSCREEN)
                else:
                    pygame.display.set_mode((larghezza, altezza), pygame.RESIZABLE)

    # Aggiorna la finestra
    pygame.display.flip()