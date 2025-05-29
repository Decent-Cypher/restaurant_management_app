import { render, screen } from '@testing-library/react';
import { MemoryRouter } from 'react-router-dom';
import NotFound from '../404';

test('renders 404 page content', () => {
  render(
    <MemoryRouter>
      <NotFound />
    </MemoryRouter>
  );
  expect(screen.getByText('404')).toBeInTheDocument();
  expect(screen.getByText(/Page Not Found/i)).toBeInTheDocument();
  expect(screen.getByText(/Return to Home/i)).toBeInTheDocument();
});