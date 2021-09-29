from types import ModuleType


def my_import(name):
    components = name.split('.')
    mod = __import__(components[0])
    for comp in components[1:]:
        mod = getattr(mod, comp)
    return mod


def test_import(vals):
    name = vals['model']
    d = vals['fields']
    klass = my_import(name)
    obj = klass(**d)
    obj.save()
