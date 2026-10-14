# راهنمای دسته‌های ادمین — 8.40.0

مسیر دسترسی: مرکز مدیریت ← دستهٔ کاری ← ابزار مستقیم. دستهٔ دیگری داخل دسته‌ها قرار ندارد. صفحهٔ انتخاب رکورد، ویرایش، ساخت، پیش‌نمایش و تأیید عملیات حفظ شده‌اند. گزارش‌های سلامت و توسعه همچنان وجود دارند؛ ابزارهایشان مستقیم در دستهٔ مناسب در دسترس‌اند.

| دسته | ابزار مستقیم |
|---|---|
| 📡 ارسال سیگنال | 40 |
| 👥 CRM و خط فروش | 18 |
| 📣 تبلیغات و کمپین‌ها | 12 |
| 💳 فروش و اشتراک‌ها | 11 |
| 🎁 جوایز و تعامل | 14 |
| 🎓 آموزش | 4 |
| 🤖 اتوماسیون مدیریتی | 3 |
| 🛡 ادمین و امنیت | 61 |

تعدادها برای موجودی کامل ابزارهاست؛ ادمین فقط موارد مجاز نقش خودش را می‌بیند. تأیید مرحلهٔ دوم و عملیات اختصاصی مالک فقط برای مدیر اصلی‌اند. کدهای قدیمی دسته‌ها به مسیر جدید هدایت می‌شوند.

## 📡 ارسال سیگنال

| ابزار | مسیر |
|---|---|
| 📡 ارسال سیگنال | `a_signal` |
| 🎨 قالب‌های سیگنال | `sig_tpl_home` |
| 📈 نتایج سیگنال | `a_signal_results` |
| 🛡 تابلوهای ریسک | `sig_exposure` |
| 👥 داشبورد تحلیلگران | `sig_analysts` |
| 🎯 مدیریت KPI Trader | `a_kpi_trader` |
| ✏️ ویرایش سیگنال | `a_signal_edit` |
| 🗑 حذف سیگنال | `a_signal_delete` |
| 🗂 دوره‌های سیگنال | `a_signal_cycle` |
| 📺 مدیریت کانال | `a_channel_center` |
| 📰 اخبار و اقتصاد | `a_market_intel` |
| 📔 ژورنال و واچ‌لیست | `a_portfolio` |
| 🕒 سیگنال‌های زمان‌بندی‌شده | `channel_schedules` |
| 📌 تابلو سیگنال کانال | `sig_board:all:0` |
| ⚙️ تنظیمات 🔔 هشدار قیمت | `ecc_mod:alerts` |
| ⚙️ تنظیمات 📊 پرتال سیگنال | `ecc_mod:portal` |
| ⚙️ تنظیمات ⭐ واچ‌لیست | `ecc_mod:watchlists` |
| ⚙️ تنظیمات 📔 ژورنال معاملاتی | `ecc_mod:journal` |
| ⚙️ تنظیمات 📡 مدیریت سیگنال | `ecc_mod:signals` |
| ⚙️ تنظیمات 🛰 ردیاب بازار | `ecc_mod:tracker` |
| ⚙️ تنظیمات 🧮 مدیریت ریسک | `ecc_mod:risk` |
| ⚙️ تنظیمات 📺 کانال‌ها | `ecc_mod:channels` |
| ⚙️ تنظیمات 💹 قیمت بازار | `ecc_mod:prices` |
| ⚙️ تنظیمات 🪙 رمزارز | `ecc_mod:crypto` |
| ⚙️ تنظیمات 🏛 سهام جهانی | `ecc_mod:stocks` |
| ⚙️ تنظیمات 🛢 انرژی و اقتصاد | `ecc_mod:energy` |
| ⚙️ تنظیمات 🗓 تقویم اقتصادی | `ecc_mod:calendar` |
| ⚙️ تنظیمات 📰 خبر و تحلیل | `ecc_mod:news` |
| ⚙️ تنظیمات 🧠 Gemini AI Sentinel | `ecc_mod:copilot` |
| ⚙️ تنظیمات 🧭 مربی رفتار و ریسک | `ecc_mod:risk_coach` |
| ⚙️ تنظیمات 🎮 معامله آزمایشی | `ecc_mod:paper_trading` |
| ⚙️ تنظیمات 🛡 نگهبان پراپ | `ecc_mod:prop_guardian` |
| ⚙️ تنظیمات 🌐 هوش بازار ۲ | `ecc_mod:market_v2` |
| ⚙️ تنظیمات 📊 عملکرد عمومی معتبر | `ecc_mod:performance` |
| 🔎 Gemini AI Sentinel | `platform_view:local_copilot` |
| 🔎 مربی رفتار و ریسک | `platform_view:risk_coach` |
| 🔎 مسابقه معامله آزمایشی | `platform_view:paper_arena` |
| 🔎 نگهبان پراپ | `platform_view:prop_guardian` |
| 🔎 هوش بازار ۲ | `platform_view:market_intelligence_v2` |
| 🔎 عملکرد عمومی قابل راستی‌آزمایی | `platform_view:public_performance` |

## 👥 CRM و خط فروش

| ابزار | مسیر |
|---|---|
| 🗂 CRM کاربران | `a_crm` |
| 🪜 خط فروش | `crm_pipeline` |
| 👥 مدیریت کاربران | `a_users` |
| 🎫 مدیریت تیکت‌ها | `a_tickets` |
| ❓ مدیریت سوالات | `a_faq` |
| 🎯 نگهداشت مشتری | `a_retention` |
| 📦 خروجی اطلاعات | `a_export_csv` |
| 📊 قیف فروش | `a_sales_funnel` |
| 🧩 گروه‌های مشتریان | `a_crm_segments` |
| 📊 داشبورد CRM | `crm_dashboard` |
| ⚙️ تنظیمات ❓ سوالات متداول | `ecc_mod:faq` |
| ⚙️ تنظیمات 🎫 پشتیبانی | `ecc_mod:support` |
| ⚙️ تنظیمات 👤 حساب کاربری | `ecc_mod:account` |
| ⚙️ تنظیمات 🗂 CRM | `ecc_mod:crm` |
| ⚙️ تنظیمات 📦 خروجی اطلاعات | `ecc_mod:exports` |
| ⚙️ تنظیمات 🧲 نگهداشت مشترک | `ecc_mod:retention` |
| ⚙️ تنظیمات 💼 صندوق کسب‌وکار | `ecc_mod:business_inbox` |
| 🔎 صندوق کسب‌وکار | `platform_view:business_inbox` |

## 📣 تبلیغات و کمپین‌ها

| ابزار | مسیر |
|---|---|
| 🚀 استودیو کمپین | `a_campaigns` |
| 📣 ارسال همگانی | `a_broadcast` |
| 📢 مرکز اعلان کانال | `a_announcement` |
| 🔗 لینک‌های جذب کانال | `a_channel_attribution` |
| 🔔 اعلان هوشمند | `owner_notification_intelligence` |
| ⚙️ تنظیمات 🔔 مرکز اعلان | `ecc_mod:notify` |
| ⚙️ تنظیمات 📣 ارسال همگانی | `ecc_mod:broadcast` |
| ⚙️ تنظیمات 🚀 استودیو کمپین | `ecc_mod:campaigns` |
| ⚙️ تنظیمات 📣 ناشر چندکاناله | `ecc_mod:publisher` |
| ⚙️ تنظیمات 🤝 مرکز همکاران | `ecc_mod:partners` |
| 🔎 ناشر چندکاناله | `platform_view:multi_channel_publisher` |
| 🔎 مرکز همکاران | `platform_view:partner_hub` |

## 💳 فروش و اشتراک‌ها

| ابزار | مسیر |
|---|---|
| 📥 پرداخت‌های معلق | `a_pending` |
| 🧾 تطبیق پرداخت | `a_reconciliation` |
| 💳 تنظیمات مالی VIP | `a_vip_settings` |
| 🧩 مدیریت پلن‌های VIP | `a_vip_plans` |
| 🎟 مدیریت تخفیف | `a_disc` |
| 👑 تمدید VIP | `a_vip_ext` |
| ♻️ تمدید هوشمند | `a_renewals` |
| 🎓 پرداخت آموزش | `a_edu_orders` |
| 💎 رشد اشتراک | `owner_subscription_growth` |
| 🎟 کدهای تخفیف عمومی | `a_public_discounts` |
| ⚙️ تنظیمات 💳 خرید و مدیریت اشتراک | `ecc_mod:subscriptions` |

## 🎁 جوایز و تعامل

| ابزار | مسیر |
|---|---|
| 🎁 جوایز کاربران | `a_user_rewards` |
| 🎁 درخواست جوایز | `a_reward_requests` |
| ⚙️ امتیاز جوایز | `a_reward_points` |
| 👥 مراحل پاداش رفرال | `a_milestones` |
| 🏆 مسابقه‌ها | `a_contest` |
| ✅ مأموریت‌ها | `a_missions` |
| 🏆 لیدربورد | `a_leaderboard` |
| 📊 آمار مسابقه‌ها | `a_contest_stats` |
| 🛡 بررسی تقلب دعوت | `refreview` |
| ⚙️ تنظیمات ✅ مأموریت‌ها | `ecc_mod:missions` |
| ⚙️ تنظیمات 🏅 لیگ و فصل | `ecc_mod:league` |
| ⚙️ تنظیمات 🎯 مسابقه‌ها | `ecc_mod:contests` |
| ⚙️ تنظیمات 🎁 امتیاز و جوایز | `ecc_mod:rewards` |
| ⚙️ تنظیمات 👥 معرفی دوستان | `ecc_mod:referrals` |

## 🎓 آموزش

| ابزار | مسیر |
|---|---|
| 📚 مدیریت آموزش | `a_edu` |
| ⚙️ تنظیمات 🎓 آموزش | `ecc_mod:edu` |
| ⚙️ تنظیمات 🏭 کارخانه محتوا | `ecc_mod:content_factory` |
| 🔎 کارخانه محتوا | `platform_view:content_factory` |

## 🤖 اتوماسیون مدیریتی

| ابزار | مسیر |
|---|---|
| 🤖 اتوماسیون مدیریتی | `a_automations` |
| 📜 گزارش اتوماسیون CRM | `crm_automation_log` |
| ⚙️ تنظیمات 🤖 اتوماسیون | `ecc_mod:automation` |

## 🛡 ادمین و امنیت

| ابزار | مسیر |
|---|---|
| 👮 مدیریت ادمین‌ها | `a_admins` |
| 🕒 شیفت ادمین‌ها | `a_shifts` |
| 🔐 تأیید مرحلهٔ دوم | `a_approvals` |
| ☀️ ادمین امروز | `a_admin_today` |
| 👑 تسک و امتیاز ادمین‌ها | `owner_kpi_center` |
| 🧠 فرمان مستقیم Gemini | `a_ai_chat_start` |
| 📊 داشبورد | `a_dashboard` |
| 🛰 مرکز عملیات | `a_mission_control` |
| 🧠 مرکز فرماندهی Gemini | `a_ai_command_center` |
| 🔎 جست‌وجوی سراسری | `a_admin_search` |
| 🧭 کنترل کامل ربات | `a_control_center` |
| 🎛 مدیریت امکانات | `a_features` |
| 📜 قوانین استفاده | `a_rules` |
| 📱 روشن/خاموش مینی‌اپ | `a_miniapp_runtime` |
| 🛟 حالت اجرا و اضطرار | `a_runtime_safety` |
| 🚨 مرکز رخدادها | `a_incidents` |
| 🧩 ماتریس قابلیت‌ها | `a_capabilities` |
| 🚀 توسعه پلتفرم بدون هزینه | `a_platform_expansion` |
| 🧠 حاکمیت عملیات | `a_ops_governance` |
| 🔎 مرکز شفافیت | `a_trust_center` |
| 💾 بکاپ و بازیابی | `a_backups` |
| 🔌 سلامت منابع قیمت | `a_provider_health` |
| 📜 لاگ ادمین | `a_logs` |
| 🧯 خطاهای Runtime | `a_runtime_logs` |
| 🩺 سلامت سیستم | `a_system_center` |
| 📊 وضعیت Google Sheets | `a_google_sheets_monitor` |
| ⚙️ کنترل کارهای پس‌زمینه | `a_job_control` |
| 🧩 پیکربندی سرویس‌ها | `a_config_wizard` |
| 🚩 انتشار امکانات | `a_feature_flags` |
| 🧱 وضعیت مهاجرت دیتابیس | `a_app_migrations` |
| 🧠 پایش عملیات | `a_ops_intelligence` |
| 🩺 عیب‌یابی زنده | `ecc_diag` |
| 🧹 نگهداری سیستم | `ecc_maintenance` |
| 📦 خروجی تنظیمات | `ecc_export` |
| ✅ فعال‌سازی کامل | `ecc_preset:full` |
| 🛡 حالت امن | `ecc_preset:safe` |
| ♻️ تنظیمات پیش‌فرض | `ecc_preset:default` |
| 🗓 عملیات تیم | `owner_team_calendar` |
| 🏆 عملکرد تیم | `owner_team_performance` |
| 🔗 عضویت اجباری | `force_join_panel` |
| ⚙️ تنظیمات 📜 قوانین استفاده | `ecc_mod:rules` |
| ⚙️ تنظیمات 🔐 حریم خصوصی | `ecc_mod:privacy` |
| ⚙️ تنظیمات 📊 داشبورد ادمین | `ecc_mod:dashboard` |
| ⚙️ تنظیمات 👮 مدیران و مجوزها | `ecc_mod:admins` |
| ⚙️ تنظیمات 🕒 شیفت مدیران | `ecc_mod:shifts` |
| ⚙️ تنظیمات 📜 Audit و لاگ | `ecc_mod:audit` |
| ⚙️ تنظیمات 🚨 مرکز رخدادها | `ecc_mod:incidents` |
| ⚙️ تنظیمات 🛡 مرکز شفافیت | `ecc_mod:trust` |
| ⚙️ تنظیمات 🩺 سلامت سرویس | `ecc_mod:health` |
| ⚙️ تنظیمات 💾 بکاپ و بازیابی | `ecc_mod:backup` |
| ⚙️ تنظیمات 🗄 دیتابیس | `ecc_mod:database` |
| ⚙️ تنظیمات 📈 مانیتورینگ | `ecc_mod:monitoring` |
| ⚙️ تنظیمات 🛡 امنیت | `ecc_mod:security` |
| ⚙️ تنظیمات 🧰 نگهداری سیستم | `ecc_mod:runtime` |
| ⚙️ تنظیمات 📱 مینی‌اپ نسل بعد | `ecc_mod:miniapp_next` |
| ⚙️ تنظیمات 🔌 پلتفرم توسعه‌دهندگان | `ecc_mod:developer_api` |
| ⚙️ تنظیمات 🏢 فضاهای کاری | `ecc_mod:workspaces` |
| ⚙️ تنظیمات 🧠 حاکمیت عملیات | `ecc_mod:governance` |
| 🔎 مینی‌اپ نسل بعد | `platform_view:miniapp_next` |
| 🔎 پلتفرم توسعه‌دهندگان | `platform_view:developer_platform` |
| 🔎 هسته فضای کاری | `platform_view:workspace_saas` |

