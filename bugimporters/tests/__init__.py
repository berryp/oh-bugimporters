import twisted

from mock import Mock


class TrackerModel(Mock):

    max_connections = 5
    tracker_name = 'Twisted',
    base_url = 'http://twistedmatrix.com/trac/'
    bug_project_name_format = '{tracker_name}'
    bitesized_type = 'keywords'
    bitesized_text = 'easy'
    documentation_type = 'keywords'
    documentation_text = 'documentation'

    def get_base_url(self):
        return self.base_url


class Bug(object):

    def __init__(self, data):
        for key, value in data.items():
            self.__setattr__(key, value)


class ReactorModel(Mock):

    running_deferreds = 0


class FakeGetPage(object):

    def get404(self, url):
        d = twisted.internet.defer.Deferred()
        d.errback(twisted.python.failure.Failure(
                twisted.web.error.Error(
                404, 'File Not Found', None)))
        return d


