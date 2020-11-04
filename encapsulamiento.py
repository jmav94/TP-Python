class CasillaDeVotacion:

    def __init__(self, identificador, pais):
        self._indentificador = identificador
        self._pais = pais
        self._region = None


    # Para que nuestra función funcione con dot notation
    # utilizamos el decorador @property
    @property
    def region(self):
        return self._region


    # Para crear un setter que funcione con dot notation
    # primero hacemos referencia al nombre de la propiedad seguido
    # de .setter (@region.setter)
    @region.setter
    def region(self, region):
        if region in self._pais:
            self._region = region
        else:
            raise ValueError(f'La región {region} no es válida en {self._pais}')


if __name__ == '__main__':
    casilla = CasillaDeVotacion(123, ['Ciudad de Mexico','Morelos','Monterrey'])
    print(casilla.region)
    casilla.region = 'Monterrey'
    print(casilla.region)
    print(casilla._region)
