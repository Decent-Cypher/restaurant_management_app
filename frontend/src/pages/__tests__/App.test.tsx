import { render, screen } from '@testing-library/react';
import '@testing-library/jest-dom';
import { MemoryRouter } from 'react-router-dom';
import App from '../App';

it('renders restaurant name and slogan', () => {
  render(
    <MemoryRouter>
      <App />
    </MemoryRouter>
  );
  expect(screen.getByText(/Restaurant name/i)).toBeInTheDocument();
  expect(screen.getByText(/Restaurant slogan/i)).toBeInTheDocument();
});