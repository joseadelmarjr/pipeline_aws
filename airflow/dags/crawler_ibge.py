from classes.Ibge import Regiao, MesoRegiao, MicroRegiao


regiao = Regiao()
mesoregiao = MesoRegiao()
microregiao = MicroRegiao()

regiao.get_data()
mesoregiao.get_data()
microregiao.get_data()

regiao.save_data("regiao.json")
mesoregiao.save_data("mesoregiao.json")
microregiao.save_data("microregiao.json")
