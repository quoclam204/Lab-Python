CREATE DATABASE QLMonAn
 
CREATE TABLE MonAn(
	MaMonAn int  NOT NULL PRIMARY KEY,
	TenMonAn nvarchar(50) NOT NULL,
	DonViTinh nvarchar(50) NULL,
	DonGia int NULL,
	Nhom int NULL)

CREATE TABLE NhomMonAn(
	MaNhom int  NOT NULL PRIMARY KEY,
	TenNhom nvarchar(50) NOT NULL)
 
INSERT INTO MonAn (TenMonAn, DonViTinh, DonGia, Nhom) VALUES (N'Gỏi thập cẩm', N'Dĩa', 120000, 1);
INSERT INTO MonAn (TenMonAn, DonViTinh, DonGia, Nhom) VALUES (N'Gỏi sứa', N'Dĩa', 140000, 1);
INSERT INTO MonAn (TenMonAn, DonViTinh, DonGia, Nhom) VALUES (N'Gỏi tai heo', N'Dĩa', 110000, 1);
INSERT INTO MonAn (TenMonAn, DonViTinh, DonGia, Nhom) VALUES (N'Tôm nướng muối ớt', N'Kg', 250000, 2);
INSERT INTO MonAn (TenMonAn, DonViTinh, DonGia, Nhom) VALUES (N'Mực nướng muối ớt', N'Kg', 290000, 2);
INSERT INTO MonAn (TenMonAn, DonViTinh, DonGia, Nhom) VALUES (N'Tôm hấp bia', N'Kg', 230000, 2);
INSERT INTO MonAn (TenMonAn, DonViTinh, DonGia, Nhom) VALUES (N'Sò nướng mỡ hành', N'Kg', 300000, 2);
INSERT INTO MonAn (TenMonAn, DonViTinh, DonGia, Nhom) VALUES (N'Bia Heniken', N'Chai', 18000, 3);
INSERT INTO MonAn (TenMonAn, DonViTinh, DonGia, Nhom) VALUES (N'Bia tiger bạc', N'Chai', 16000, 3);
INSERT INTO MonAn (TenMonAn, DonViTinh, DonGia, Nhom) VALUES (N'Coca', N'Lon', 16000, 3);
INSERT INTO MonAn (TenMonAn, DonViTinh, DonGia, Nhom) VALUES (N'Lẩu hải sản', N'Nồi', 220000, 4);
INSERT INTO MonAn (TenMonAn, DonViTinh, DonGia, Nhom) VALUES (N'Lẩu cá tầm', N'Nồi', 270000, 4);
INSERT INTO MonAn (TenMonAn, DonViTinh, DonGia, Nhom) VALUES (N'Lẩu gà lá é', N'nồi', 250000, 4);


INSERT NhomMonAn (MaNhom, TenNhom) VALUES (1, N'Khai vị')
INSERT NhomMonAn (MaNhom, TenNhom) VALUES (2, N'Hải sản')
INSERT NhomMonAn (MaNhom, TenNhom) VALUES (3, N'Bia - Nước ngọt')
INSERT NhomMonAn (MaNhom, TenNhom) VALUES (4, N'Lẩu')



SELECT * FROM NhomMonAn;
SELECT * FROM MonAn;

DROP TABLE IF EXISTS MonAn;

-- Tạo lại bảng MonAn với MaMonAn là cột tự động tăng
CREATE TABLE MonAn(
    MaMonAn INT IDENTITY(1,1) NOT NULL PRIMARY KEY,  -- Tạo MaMonAn tự động tăng
    TenMonAn NVARCHAR(50) NOT NULL,
    DonViTinh NVARCHAR(50) NULL,
    DonGia INT NULL,
    Nhom INT NULL
);

