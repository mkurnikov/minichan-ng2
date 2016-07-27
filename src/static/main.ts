import {bootstrap} from "@angular/platform-browser-dynamic";
import {HTTP_PROVIDERS} from "@angular/http";
import {provideForms, disableDeprecatedForms} from "@angular/forms";

import {AppComponent} from "./app.component";


bootstrap(AppComponent, [
    disableDeprecatedForms(),
    provideForms(),
    HTTP_PROVIDERS
])
    .catch((err: any) => console.error(err));