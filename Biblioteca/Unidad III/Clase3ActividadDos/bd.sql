CREATE TABLE IF NOT EXISTS public.producto
(
    id integer NOT NULL DEFAULT nextval('producto_id_seq'::regclass),
    nombre character varying COLLATE pg_catalog."default" NOT NULL,
    descripcion text COLLATE pg_catalog."default",
    precio double precision NOT NULL,
    stock integer NOT NULL,
    CONSTRAINT producto_pkey PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS public.usuario
(
    id bigint NOT NULL DEFAULT nextval('usuario_id_seq'::regclass),
    nombre character varying COLLATE pg_catalog."default" NOT NULL,
    passw character varying COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT usuario_pkey PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS public.pedido
(
    id integer NOT NULL DEFAULT nextval('pedido_id_seq'::regclass),
    fecha date NOT NULL,
    fk_id_autor bigint NOT NULL,
    entregado boolean NOT NULL,
    CONSTRAINT pedido_pkey PRIMARY KEY (id),
    CONSTRAINT fk_id_usuario FOREIGN KEY (fk_id_autor)
        REFERENCES public.usuario (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
);

CREATE TABLE IF NOT EXISTS public.productopedido
(
    fk_id_producto bigint NOT NULL,
    fk_id_pedido bigint NOT NULL,
    cantidad bigint NOT NULL,

    CONSTRAINT fk_id_producto FOREIGN KEY (fk_id_producto)
        REFERENCES public.producto (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION,
   CONSTRAINT fk_id_pedido FOREIGN KEY (fk_id_pedido)
        REFERENCES public.pedido (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
);