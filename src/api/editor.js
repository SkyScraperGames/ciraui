import config from '../env/config';

export function save(title, text) {
  const formData = new URLSearchParams();
  formData.append('title', title);
  formData.append('text', text);

  return fetch(`${config.api}/editor/saveeditor`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/x-www-form-urlencoded',
    },
    body: formData,
    credentials: 'include',
  });
}

export function load(name) {
  return fetch(`${config.api}/editor/open/${name}`, {
    credentials: 'include',
  });
}

export function history(name) {
  return fetch(`${config.api}/editor/diff/${name}`, {
    credentials: 'include',
  });
}

export function deleteFile(name) {
  return fetch(`${config.api}/editor/delete/${name}`, {
    credentials: 'include',
  });
}
