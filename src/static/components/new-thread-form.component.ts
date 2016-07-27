import {Component} from "@angular/core";


export class Thread {
    constructor (
        public subject: string,
        public text: string,
        public picture?: string
    ) {}
}

@Component({
    moduleId: module.id,
    selector: 'new-thread-form',
    templateUrl: 'new-thread-form.component.html'
})
export class NewThreadFormComponent {
    thread: Thread = new Thread('', '', '');

    maxMessageLength: number = 1000;

    get placeholder(): string {
        return 'Ваше сообщение. Максимальная длина ' + this.maxMessageLength + '.'
    };

    diagnostics = () => {
        return JSON.stringify(this.thread);
    }
}