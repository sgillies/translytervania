from pyramid.config import Configurator
from translytervania.resources import Root

def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(root_factory=Root, settings=settings)
    config.add_view('translytervania.views.form',
                    context='translytervania:resources.Root',
                    renderer='translytervania:templates/form.pt')
    config.add_static_view('static', 'translytervania:static', cache_max_age=3600)
    return config.make_wsgi_app()
