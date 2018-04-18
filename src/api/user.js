import config from '../env/config';

export function login(username, password, remember) {
  const formData = new URLSearchParams();
  formData.set('email', username);
  formData.set('password', password);
  formData.set('remember', remember);

  return fetch(`${config.api}/user/login`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/x-www-form-urlencoded',
    },
    body: formData,
    credentials: 'include',
  });
}

export function register(username, recoveryEmail, password) {
  const formData = new URLSearchParams();
  formData.set('email', username);
  formData.set('recoveryEmail', recoveryEmail);
  formData.set('password', password);

  return fetch(`${config.api}/user/signup`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/x-www-form-urlencoded',
    },
    body: formData,
    credentials: 'include',
  });
}

export function logout() {
  return fetch(`${config.api}/user/logout`, {
    method: 'POST',
    credentials: 'include',
  });
}

export function profile() {
  return fetch(`${config.api}/user/profile`, {
    credentials: 'include',
  });
}

export function resetPassword(oldPassword, newPassword) {
  const formData = new URLSearchParams();
  formData.set('oldpassword', oldPassword);
  formData.set('password', newPassword);

  return fetch(`${config.api}/user/changepassword`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/x-www-form-urlencoded',
    },
    body: formData,
    credentials: 'include',
  });
}

export function forgotPassword(username, recoveryEmail) {
  const formData = new URLSearchParams();
  formData.set('email', username);
  formData.set('recoveryEmail', recoveryEmail);

  return fetch(`${config.api}/user/forgotpassword`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/x-www-form-urlencoded',
    },
    body: formData,
    credentials: 'include',
  });
}

export function changePassword(username, recoveryPin, password) {
  const formData = new URLSearchParams();
  formData.set('email', username);
  formData.set('recoveryPin', recoveryPin);
  formData.set('password', password);

  return fetch(`${config.api}/user/recoverpassword`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/x-www-form-urlencoded',
    },
    body: formData,
    credentials: 'include',
  });
}

export function changeEmail(recoveryEmail, password) {
  const formData = new URLSearchParams();
  formData.set('recoveryEmail', recoveryEmail);
  formData.set('password', password);

  return fetch(`${config.api}/user/changerecoveryemail`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/x-www-form-urlencoded',
    },
    body: formData,
    credentials: 'include',
  });
}
