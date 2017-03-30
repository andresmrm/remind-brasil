#!/usr/bin/env python
# coding: utf-8

"""
Gera um arquivo Remind com estações do ano.
"""

import ephem
from pytz import timezone


def formata_data(r):
    return timezone('UTC').localize(r.datetime()).astimezone(
        timezone('Brazil/East')).date()


if __name__ == '__main__':
    arq = open('estacoes.remind', 'w')
    for ano in range(2000, 2051):
        ano = str(ano)
        print(ano)
        estacoes = [
            (ephem.next_solstice(ano), 'Inverno'),
            (ephem.next_solstice(ano + '/7'), 'Verão'),
            (ephem.next_equinox(ano), 'Outono'),
            (ephem.next_equinox(ano + '/7'), 'Primavera'),
        ]
        for data, msg in estacoes:
            arq.write('REM {data} MSG {msg}\n'.format(
                data=formata_data(data), msg=msg))
    arq.close()
