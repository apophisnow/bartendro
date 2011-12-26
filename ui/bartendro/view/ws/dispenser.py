# -*- coding: utf-8 -*-
from werkzeug.utils import redirect
from werkzeug.exceptions import BadRequest, ServiceUnavailable
from bartendro.utils import session, local, expose, validate_url, url_for, render_text
from bartendro.model.drink import Drink
from bartendro.model.booze import Booze
from bartendro.form.booze import BoozeForm

@expose('/ws/dispenser/<int:disp>/on')
def ws_dispenser_on(request, disp):
    driver = local.application.driver
    count = driver.count()
    if disp < 1 or disp > count: raise BadRequest("Invalid dispenser %d selected. We've got %d." % (disp, count))

    ret = driver.start(disp, 254)
    if ret == 0:
        return render_text("ok\n")
    else:
        raise ServiceUnavailable("Error: %s (%d)" % (driver.get_error(), ret))

@expose('/ws/dispenser/<int:disp>/off')
def ws_dispenser_off(request, disp):
    driver = local.application.driver
    count = driver.count()
    if disp < 1 or disp > count: raise BadRequest("Invalid dispenser %d selected. We've got %d." % (disp, count))

    ret = driver.stop(disp)
    if ret == 0:
        return render_text("ok\n")
    else:
        raise ServiceUnavailable("Error: %s (%d)" % (driver.get_error(), ret))