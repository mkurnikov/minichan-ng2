import {Component} from "@angular/core";
import {NewThreadFormComponent} from "./components/new-thread-form.component";


@Component({
    moduleId: module.id,
    selector: 'app',
    templateUrl: 'app.component.html',
    directives: [NewThreadFormComponent]
})
export class AppComponent {
    text: string = 'Hello, world';
}