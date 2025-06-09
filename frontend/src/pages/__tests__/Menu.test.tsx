import { render, screen } from '@testing-library/react';
import Menu from '../Menu';
import { MemoryRouter } from 'react-router-dom';

test('renders menu categories and items', () => {
  render(
      <MemoryRouter>
        <Menu />
      </MemoryRouter>
    );
  expect(screen.getByText(/Appetizers/i)).toBeInTheDocument();
  expect(screen.getByText(/Main Courses/i)).toBeInTheDocument();
  expect(screen.getByText(/Desserts/i)).toBeInTheDocument();
  expect(screen.getByText(/Spring Rolls/i)).toBeInTheDocument();
});