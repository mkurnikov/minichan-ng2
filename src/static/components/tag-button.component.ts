import {Component, OnInit, Input} from '@angular/core';

@Component({
    moduleId: module.id,
    selector: 'editor-tag-button',
    templateUrl: 'tag-button.component.html'
})
export class TagButtonComponent {
    @Input() textarea: HTMLTextAreaElement;

    @Input() img: string;
    @Input() tagName: string;

    addTag = () => {
        this.textarea.textContent += this.getFormattedTag();
    };

    getFormattedTag = () => {
        return '[' + this.tagName + '][' + this.tagName + ']'
    }
}