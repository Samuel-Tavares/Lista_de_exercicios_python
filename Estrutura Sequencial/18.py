megabits = 8
um_minuto_em_segundos = 60

tamanho_arquivo = float(input('Informe o tamanho do arquivo para Download:'))
velocidade_mbps = float(input('Informe a velocidade em Mbps: '))


tempo_download = tamanho_arquivo / (velocidade_mbps / megabits)
minutos_download = tempo_download // um_minuto_em_segundos
segundos_download = tempo_download % um_minuto_em_segundos

print(f'O download será feito em {minutos_download:.0f} minuto e '
      f'{segundos_download:.0f} segundos.')
