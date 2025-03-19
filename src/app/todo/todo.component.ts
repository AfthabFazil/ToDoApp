import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';

interface Task {
  name: string;
  completed: boolean;
  priority: 'High' | 'Medium' | 'Low';
  dueDate: string;
}

@Component({
  selector: 'app-todo',
  templateUrl: './todo.component.html',
  styleUrls: ['./todo.component.css'],
  standalone: true,
  imports: [CommonModule, FormsModule],
})
export class TodoComponent {
  newTask: string = '';
  newTaskPriority: 'High' | 'Medium' | 'Low' = 'Medium';
  newTaskDueDate: string = '';
  tasks: Task[] = [];
  filter: 'All' | 'Active' | 'Completed' = 'All';
  sortBy: 'priority' | 'dueDate' = 'priority';

  addTask() {
    if (this.newTask.trim()) {
      this.tasks.push({
        name: this.newTask.trim(),
        completed: false,
        priority: this.newTaskPriority,
        dueDate: this.newTaskDueDate,
      });
      this.newTask = '';
      this.newTaskDueDate = '';
      this.sortTasks();
    }
  }

  toggleCompletion(index: number) {
    this.tasks[index].completed = !this.tasks[index].completed;
  }

  deleteTask(index: number) {
    this.tasks.splice(index, 1);
  }

  sortTasks() {
    this.tasks.sort((a, b) => {
      if (this.sortBy === 'priority') {
        const priorityOrder = { High: 1, Medium: 2, Low: 3 };
        return priorityOrder[a.priority] - priorityOrder[b.priority];
      } else {
        return new Date(a.dueDate).getTime() - new Date(b.dueDate).getTime();
      }
    });
  }

  get filteredTasks() {
    return this.tasks.filter((task) => {
      if (this.filter === 'Active') return !task.completed;
      if (this.filter === 'Completed') return task.completed;
      return true;
    });
  }
}
