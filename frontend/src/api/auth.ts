export const login = async (type, username, password) => {
  const url = `http://localhost:8000/api/accounts/${type}/login/`; // type = 'staff' or 'diner'
  const formData = new URLSearchParams();
  formData.append('username', username);
  formData.append('password', password);

  const res = await fetch(url, {
    method: 'POST',
    body: formData,
    credentials: 'include', // Important: sends session cookie
    headers: {
      'Content-Type': 'application/x-www-form-urlencoded',
    },
  });

  return res.json();
};

export const logout = async () => {
  const res = await fetch('http://localhost:8000/api/accounts/logout/', {
    method: 'POST',
    credentials: 'include',
  });

  if (!res.ok) throw new Error('Logout failed');
  return res.json();
};

export const getUserInfo = async () => {
  const res = await fetch('http://localhost:8000/api/accounts/protected/', {
    method: 'GET',
    credentials: 'include',
  });

  if (!res.ok) throw new Error('Not logged in');
  return res.json();
};
