export const login = async (type, username, password) => {
  const formData = new FormData();
  formData.append("username", username);
  formData.append("password", password);

  const res = await fetch(`http://localhost:8000/api/accounts/${type}/login/`, {
    method: "POST",
    credentials: "include",
    body: formData, // <-- send FormData here
    // Don't set Content-Type manually! The browser sets it with the proper boundary
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
