import { render, screen, fireEvent, waitFor } from '@testing-library/react';
import { MemoryRouter } from 'react-router-dom';
import Order from '../Order';

beforeEach(() => {
  global.fetch = jest.fn((url) => {
    if (url.includes('/menus/')) {
      return Promise.resolve({ json: () => Promise.resolve([{ id: 1, name: 'Pizza', image: 'pizza.jpg', description: 'desc' }]) });
    }
    if (url.includes('/menu-items/')) {
      return Promise.resolve({ json: () => Promise.resolve([{ id: 1, name: 'Margherita', price: '10000', image: 'm.jpg', menu: 1 }]) });
    }
    return Promise.reject('Unknown API');
  }) as jest.Mock;
});

test('renders service type options', () => {
  render(
      <MemoryRouter>
        <Order />
      </MemoryRouter>
    );
  expect(screen.getByText(/Choose your service type/i)).toBeInTheDocument();
});

test('validates table number input', () => {
  render(
      <MemoryRouter>
        <Order />
      </MemoryRouter>
    );
  fireEvent.click(screen.getByLabelText('Dine-in'));
  const input = screen.getByPlaceholderText(/Enter your table number/i);
  fireEvent.change(input, { target: { value: '25' } });
  expect(screen.getByText(/Please enter a number between 1 and 20/i)).toBeInTheDocument();
});

test('loads menu categories and popular dishes', async () => {
  render(
      <MemoryRouter>
        <Order />
      </MemoryRouter>
    );
  await waitFor(() => {
    expect(screen.getByText(/Pizza/i)).toBeInTheDocument();
    expect(screen.getByText(/Margherita/i)).toBeInTheDocument();
  });
});