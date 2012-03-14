# This file is part of OpenHatch.
# Copyright (C) 2010 OpenHatch, Inc.
# Copyright (C) 2012 Berry Phillips.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import dateutil.parser
import StringIO

from decorator import decorator


def string2naive_datetime(s):
    time_zoned = dateutil.parser.parse(s)
    if time_zoned.tzinfo:
        d_aware = time_zoned.astimezone(dateutil.tz.tzutc())
        d = d_aware.replace(tzinfo=None)
    else:
        d = time_zoned  # best we can do
    return d


def cached_property(func):
    """Decorator that returns a cached property that is calculated by function func"""
    def get(self):
        try:
            return self._property_cache[func]
        except AttributeError:
            self._property_cache = {}
            value = self._property_cache[func] = func(self)
            return value
        except KeyError:
            value = self._property_cache[func] = func(self)
            return value

    return property(get)


def wrap_file_object_in_utf8_check(f):
    ### For now, this does the horrifying thing of reading in the whole file.
    ### Better ways would be apprediated.
    bytes = f.read()
    if type(bytes) == unicode:
        as_unicode = bytes
    else:
        as_unicode = unicode(bytes, 'utf-8-sig')
    as_utf8 = as_unicode.encode('utf-8')
    return StringIO.StringIO(as_utf8)


@decorator
def unicodify_strings_when_inputted(func, *args, **kwargs):
    '''Decorator that makes sure every argument passed in that is
    a string-esque type is turned into a Unicode object. Does so
    by decoding UTF-8 byte strings into Unicode objects.'''
    args_as_list = list(args)
    # first, *args
    for i in range(len(args)):
        arg = args[i]
        if type(arg) is str:
            args_as_list[i] = unicode(arg, 'utf-8')

    # then, **kwargs
    for key in kwargs:
        arg = kwargs[key]
        if type(arg) is str:
            kwargs[key] = unicode(arg, 'utf-8')

    return func(*args_as_list, **kwargs)
