CREATE TABLE IF NOT EXISTS public.producto
(
    id integer NOT NULL DEFAULT nextval('producto_id_seq'::regclass),
    nombre character varying COLLATE pg_catalog."default" NOT NULL,
    "desc " text COLLATE pg_catalog."default",
    precio double precision NOT NULL,
    CONSTRAINT producto_pkey PRIMARY KEY (id)
)

CREATE TABLE IF NOT EXISTS public.usuario
(
    id bigint NOT NULL DEFAULT nextval('usuario_id_seq'::regclass),
    nombre character varying COLLATE pg_catalog."default" NOT NULL,
    passw character varying COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT usuario_pkey PRIMARY KEY (id)
)

--La dificultad que tenemos es la imposibilidad de reflejar fielmente la relación que existe
-- entre Producto y Pedido. Esa relación de agregación necesita de una FK, que se verá en
-- la clase siguiente. 


-- Si el grupo está en un nivel avanzado, es posible introducirla ahora mismo.
-- En ese caso, la Actividad 2 de la Clase 2, Unidad III debe incluir directamente el sistema ABM
-- correctamente resuelto en su totalidad, en la Clase 3, Actividad 1. 
-- Será necesario utilizar una tabla de intersección, ProductoPedido, para modelizar
-- una realación de muchos a muchos.