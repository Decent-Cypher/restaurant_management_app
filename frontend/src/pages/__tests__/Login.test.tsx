import { render, screen, fireEvent, waitFor } from '@testing-library/react';
import { MemoryRouter } from 'react-router-dom';
import Login from '../Login';

test('renders login form with username and password inputs', () => {
  render(
    <MemoryRouter>
      <Login />
    </MemoryRouter>
  );
  expect(screen.getByLabelText(/Email or Username/i)).toBeInTheDocument();
  expect(screen.getByLabelText(/^Password$/)).toBeInTheDocument();
});

test('shows error on failed login', async () => {
  global.fetch = jest.fn(() =>
    Promise.resolve({
      ok: false,
      json: () => Promise.resolve({ error: 'Invalid credentials' }),
    })
  ) as jest.Mock;

  render(
      <MemoryRouter>
        <Login />
      </MemoryRouter>
    );
  fireEvent.change(screen.getByLabelText(/Email or Username/i), {
    target: { value: 'wronguser' },
  });
  fireEvent.change(screen.getByLabelText(/^Password$/), {
    target: { value: 'wrongpass' },
  });
  fireEvent.click(screen.getByRole('button', { name: /Login/i }));

  await waitFor(() => screen.getByText(/Invalid credentials/i));
  expect(screen.getByText(/Invalid credentials/i)).toBeInTheDocument();
});