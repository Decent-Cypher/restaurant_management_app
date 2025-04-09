<div align='center'>

## Frontend construction site

</div>

Written with React, (preferably) TypeScript, Tailwind CSS. Built with Vite.

## To get this running (separately without Docker)

```bash
npm install
```
```bash
npm run dev
```

## To add a page or route

Pages go to `/src/pages`. Reusable components such as button, navbar, menu item, etc. go to `/src/components`.

Once done, manually add the route to `components/Header.tsx` and `routing.tsx`.

## To style anything

Tailwind lets you style components using class name, check it out [in the docs](https://tailwindcss.com/docs/). Gone are the days when we had to open the component code and style sheet side-by-side :D

`/src/styles/global.css` is for global styling, say theme color or fonts.