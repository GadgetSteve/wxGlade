# codegen.py: code generator functions for wxSpinCtrl objects
#
# Copyright (c) 2002-2003 Alberto Griggio <albgrig@tiscalinet.it>
# License: MIT (see license.txt)
# THIS PROGRAM COMES WITH NO WARRANTY

import common

def python_code_generator(obj):
    """\
    function that generates python code for wxSpinCtrl objects.
    """
    pygen = common.code_writers['python']
    prop = obj.properties
    id_name, id = pygen.generate_code_id(obj)
    value = prop.get('value', '')
    try: min_v, max_v = [ s.strip() for s in \
                          prop.get('range', '0, 100').split(',') ]
    except: min_v, max_v = '0', '100'
    
    if not obj.parent.is_toplevel: parent = 'self.%s' % obj.parent.name
    else: parent = 'self'
    style = prop.get("style")
    if style: style = ", style=%s" % style
    else: style = ''
    init = []
    if id_name: init.append(id_name)
    init.append('self.%s = %s(%s, %s, "%s", min=%s, max=%s%s)\n' %
                (obj.name, obj.klass, parent, id, value, min_v, max_v, style))
    props_buf = pygen.generate_common_properties(obj)
    return init, props_buf, []


def xrc_code_generator(obj):
    xrcgen = common.code_writers['XRC']
    class SpinCtrlXrcObject(xrcgen.DefaultXrcObject):
        def write_property(self, name, val, outfile, tabs):
            if name == 'range':
                try: min, max = val.split(',')
                except ValueError: pass
                else:
                    tab_s = '    '*tabs
                    outfile.write(tab_s + '<min>%s</min>\n' % min)
                    outfile.write(tab_s + '<max>%s</max>\n' % max)
            else:
                xrcgen.DefaultXrcObject.write_property(self, name, val,
                                                       outfile, tabs)

    # end of class SpinCtrlXrcObject
    
    return SpinCtrlXrcObject(obj)


def cpp_code_generator(obj):
    """\
    function that generates C++ code for wxSpinCtrl objects.
    """
    cppgen = common.code_writers['C++']
    prop = obj.properties
    id_name, id = cppgen.generate_code_id(obj)
    if id_name: ids = [ id_name ]
    else: ids = []
    value = prop.get('value', '')
    try: min_v, max_v = [ s.strip() for s in \
                          prop.get('range', '0, 100').split(',') ]
    except: min_v, max_v = '0', '100'
    
    if not obj.parent.is_toplevel: parent = '%s' % obj.parent.name
    else: parent = 'this'
    style = prop.get('style')
    if not style: style = 'wxSP_ARROW_KEYS'
    init = ['%s = new %s(%s, %s, "%s", wxDefaultPosition, wxDefaultSize,'
            ' %s, %s, %s);\n' %
            (obj.name, obj.klass, parent, id, value, style, min_v, max_v)]
    props_buf = cppgen.generate_common_properties(obj)
    return init, ids, props_buf, []


def initialize():
    common.class_names['EditSpinCtrl'] = 'wxSpinCtrl'
    
    pygen = common.code_writers.get('python')
    if pygen:
        pygen.add_widget_handler('wxSpinCtrl', python_code_generator)
    xrcgen = common.code_writers.get("XRC")
    if xrcgen:
        xrcgen.add_widget_handler('wxSpinCtrl', xrc_code_generator)
    cppgen = common.code_writers.get('C++')
    if cppgen:
        cppgen.add_widget_handler('wxSpinCtrl', cpp_code_generator,
                                  extra_headers=['<wx/spinctrl.h>'])
