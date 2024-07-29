import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';

@Component({
  selector: 'app-todo',
  templateUrl: './todo.component.html',
  styleUrls: ['./todo.component.css'],
  standalone: true,
  imports: [CommonModule, FormsModule], // Import CommonModule and FormsModule
})
export class TodoComponent {
  newTask: string = '';
  tasks: { name: string, completed: boolean }[] = [];

  addTask() {
    if (this.newTask.trim()) {
      this.tasks.push({ name: this.newTask.trim(), completed: false });
      this.newTask = '';
    }
  }

  toggleCompletion(index: number) {
    this.tasks[index].completed = !this.tasks[index].completed;
  }

  deleteTask(index: number) {
    this.tasks.splice(index, 1);
  }
}