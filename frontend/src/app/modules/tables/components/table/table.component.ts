import { CommonModule } from '@angular/common';
import { Component, EventEmitter, Input, Output } from '@angular/core';

@Component({
  selector: 'app-table',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './table.component.html',
  styleUrl: './table.component.css'
})
export class TableComponent {
  @Input({ required: true }) table: number = 1;

  @Output() viewTable = new EventEmitter();

  sendNumberTableHandler() {
    this.viewTable.emit(this.table)
  }
}
