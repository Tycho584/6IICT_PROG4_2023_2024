# Maak voor deze oefen mee gebruik van onderstaande dictionary van dictionaries.
spelinfo = {
    'speler1': {
        'naam': 'Alice',
        'positie': {
            'x': 10,
            'y': 5
        },
        'inventaris': {
            'wapen': 'zwaard',
            'goud': 50
        }
    },
    'speler2': {
        'naam': 'Bob',
        'positie': {
            'x': 2,
            'y': 8
        },
        'inventaris': {
            'wapen': 'boog',
            'goud': 9999999999
        }
    }
}
print(spelinfo['speler2']['naam'])
print(spelinfo['speler1']['positie'])
print(spelinfo['speler2']['inventaris']['wapen'])

spelinfo['speler2']['inventaris']['goud'] = 0
print(spelinfo['speler2']['inventaris']['goud'])
spelinfo['speler2']['hacker'] = False
spelinfo['speler2']['hacker'] = True
print(spelinfo)
spelinfo['speler1']['inventaris']['bepansering'] = "schild"
print(spelinfo)