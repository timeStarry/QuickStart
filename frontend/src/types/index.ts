export interface Todo {
  id: number;
  title: string;
  description?: string;
  is_completed: boolean;
  due_date?: string;
  created_at: string;
  updated_at?: string;
}

export interface Widget {
  id: number;
  type: string;
  title?: string;
  config: Record<string, any>;
  position: { x: number; y: number };
  created_at: string;
  updated_at?: string;
} 