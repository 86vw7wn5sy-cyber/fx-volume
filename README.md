# FX Volume - منصة تحليل الفوركس بالذكاء الاصطناعي

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![Status: Active](https://img.shields.io/badge/status-active-success.svg)](#)

## 🎯 نبذة عن المشروع

**FX Volume** منصة متقدمة لتحليل سوق الفوركس تجمع بين:
- 📊 تحليل فني متقدم
- 🤖 نماذج الذكاء الاصطناعي للتنبؤ
- 📈 رسوم بيانية تفاعلية
- 💡 إشارات تداول احتمالية
- 🛡️ إدارة مخاطر شاملة

## ⚠️ تحذير قانوني

هذه المنصة توفر تحليلات احتمالية فقط وليست ضمانًا للأرباح. سوق الفوركس ي��طوي على مخاطر عالية. استخدمها على مسؤوليتك الخاصة.

## 📋 المتطلبات

- Python 3.9+
- Node.js 16+
- PostgreSQL أو SQLite
- Redis (اختياري)

## 🚀 التثبيت

### 1. استنساخ المستودع
```bash
git clone https://github.com/86vw7wn5sy-cyber/fx-volume.git
cd fx-volume
```

### 2. تثبيت متطلبات Backend
```bash
cd backend
python -m venv venv
source venv/bin/activate  # أو venv\Scripts\activate على Windows
pip install -r requirements.txt
```

### 3. تثبيت متطلبات Frontend
```bash
cd ../frontend
npm install
```

### 4. إعداد متغيرات البيئة
```bash
# في مجلد backend
cp .env.example .env
# عدّل .env بمفاتيح API الخاصة بك
```

### 5. تشغيل قاعدة البيانات
```bash
cd ../backend
alembic upgrade head
```

## 🎮 البدء السريع

### تشغيل Backend
```bash
cd backend
python -m uvicorn app.main:app --reload
```
يعمل على: http://localhost:8000

### تشغيل Frontend
```bash
cd frontend
npm start
```
يعمل على: http://localhost:3000

## 📁 هيكل المشروع

```
fx-volume/
├── backend/
│   ├── app/
│   │   ├��─ main.py
│   │   ├── models/
│   │   ├── routes/
│   │   ├── services/
│   │   ├── ml/
│   │   └── utils/
│   ├── tests/
│   ├── requirements.txt
│   ├── .env.example
│   └── alembic/
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   ├── pages/
│   │   ├── services/
│   │   ├── styles/
│   │   └── App.js
│   ├── public/
│   └── package.json
├── docs/
├── docker-compose.yml
└── README.md
```

## 🌟 المميزات الرئيسية

### 1. لوحة التحكم
- عرض أسعار أزواج الفوركس الرئيسية
- رسوم بيانية تفاعلية (Candlestick, Line charts)
- مؤشرات فنية (RSI, MACD, Bollinger Bands, Moving Averages)

### 2. التحليل الفني
- حساب مستويات الدعم والمقاومة
- تحليل الاتجاه (Trend Analysis)
- تحليل الأنماط (Pattern Recognition)
- تحليل حجم التداول والسيولة

### 3. الذكاء الاصطناعي
- نموذج LSTM للتنبؤ بالأسعار
- نموذج Random Forest لتصنيف الإشارات
- تحسين مستمر من البي��نات التاريخية

### 4. الإشارات والتنبيهات
- إشارات شراء وبيع احتمالية
- نسبة دقة التنبيهات
- تنبيهات فورية (Email, Dashboard)

### 5. إدارة المخاطر
- حساب نسب المخاطر/العائد
- تحديد مستويات Stop Loss و Take Profit
- إدارة حجم المركز

## 🔌 API Endpoints

### الأسعار والبيانات
```
GET  /api/v1/prices/{pair}           # آخر سعر لزوج معين
GET  /api/v1/history/{pair}          # السجل التاريخي
GET  /api/v1/indicators/{pair}       # المؤشرات الفنية
```

### التحليل
```
GET  /api/v1/analysis/{pair}         # تحليل شامل
GET  /api/v1/signals/{pair}          # الإشارات الحالية
GET  /api/v1/risk-management/{pair}  # إدارة المخاطر
```

### الحسابات
```
GET  /api/v1/accounts/me             # بيانات الحساب
POST /api/v1/accounts/settings       # تحديث الإعدادات
GET  /api/v1/accounts/history        # سجل التحليلات
```

## 📊 مصادر البيانات

- **Alpha Vantage** - أسعار الفوركس والمؤشرات
- **OANDA API** - بيانات فوركس عالية الجودة
- **Yahoo Finance** - بيانات تاريخية
- **IEX Cloud** - بيانات إضافية

## 🧪 الاختبارات

```bash
# تشغيل جميع الاختبارات
cd backend
pytest

# اختبارات محددة
pytest tests/test_indicators.py
pytest tests/test_ml_models.py
pytest tests/test_api.py

# تقرير التغطية
pytest --cov=app tests/
```

## 🐳 Docker

```bash
# بناء الصور
docker-compose build

# تشغيل المشروع
docker-compose up
```

## 📚 التوثيق

شاهد [DOCUMENTATION.md](docs/DOCUMENTATION.md) للتوثيق المفصل.

## 🤝 المساهمة

نرحب بمساهماتك! شاهد [CONTRIBUTING.md](CONTRIBUTING.md)

## 📝 الترخيص

هذا المشروع مرخص تحت رخصة MIT. شاهد [LICENSE](LICENSE)

## 📧 التواصل

للأسئلة والاقتراحات: [email protected]

---

**آخر تحديث:** سبتمبر 2026
**الإصدار:** 1.0.0