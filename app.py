<!DOCTYPE html>
<!-- saved from url=(0071)https://github.com/fastabyq/-Deploy_ke_Streamlit_Cloud/blob/main/app.py -->
<html lang="en" data-color-mode="auto" data-light-theme="light" data-dark-theme="dark" data-a11y-animated-images="system" data-a11y-link-underlines="true" data-js-focus-visible="" data-turbo-loaded="" aria-busy="true"><head><meta http-equiv="Content-Type" content="text/html; charset=UTF-8"><style type="text/css">.turbo-progress-bar {
  position: fixed;
  display: block;
  top: 0;
  left: 0;
  height: 3px;
  background: #0076ff;
  z-index: 2147483647;
  transition:
    width 300ms ease-out,
    opacity 150ms 150ms ease-in;
  transform: translate3d(0, 0, 0);
}
</style>
    
  
  
  
  
  
  

  

  <link crossorigin="anonymous" media="all" rel="stylesheet" href="./app_files/light_experimental-d0637bbdaa51.css"><link crossorigin="anonymous" media="all" rel="stylesheet" href="./app_files/dark_experimental-b3eb81810916.css"><link data-color-theme="light_high_contrast" crossorigin="anonymous" media="all" rel="stylesheet" data-href="https://github.githubassets.com/assets/light_high_contrast_experimental-10abdc3747c3.css"><link data-color-theme="light_colorblind" crossorigin="anonymous" media="all" rel="stylesheet" data-href="https://github.githubassets.com/assets/light_colorblind_experimental-49cf0efe982a.css"><link data-color-theme="light_colorblind_high_contrast" crossorigin="anonymous" media="all" rel="stylesheet" data-href="https://github.githubassets.com/assets/light_colorblind_high_contrast_experimental-e379dad4f96f.css"><link data-color-theme="light_tritanopia" crossorigin="anonymous" media="all" rel="stylesheet" data-href="https://github.githubassets.com/assets/light_tritanopia_experimental-73918b3a2f64.css"><link data-color-theme="light_tritanopia_high_contrast" crossorigin="anonymous" media="all" rel="stylesheet" data-href="https://github.githubassets.com/assets/light_tritanopia_high_contrast_experimental-b843cf381204.css"><link data-color-theme="dark_high_contrast" crossorigin="anonymous" media="all" rel="stylesheet" data-href="https://github.githubassets.com/assets/dark_high_contrast_experimental-5748739a6b50.css"><link data-color-theme="dark_colorblind" crossorigin="anonymous" media="all" rel="stylesheet" data-href="https://github.githubassets.com/assets/dark_colorblind_experimental-c45cc62af0e7.css"><link data-color-theme="dark_colorblind_high_contrast" crossorigin="anonymous" media="all" rel="stylesheet" data-href="https://github.githubassets.com/assets/dark_colorblind_high_contrast_experimental-32b00a22b284.css"><link data-color-theme="dark_tritanopia" crossorigin="anonymous" media="all" rel="stylesheet" data-href="https://github.githubassets.com/assets/dark_tritanopia_experimental-dfdb41647a89.css"><link data-color-theme="dark_tritanopia_high_contrast" crossorigin="anonymous" media="all" rel="stylesheet" data-href="https://github.githubassets.com/assets/dark_tritanopia_high_contrast_experimental-66cec90757f5.css"><link data-color-theme="dark_dimmed" crossorigin="anonymous" media="all" rel="stylesheet" data-href="https://github.githubassets.com/assets/dark_dimmed_experimental-a537244628ca.css"><link data-color-theme="dark_dimmed_high_contrast" crossorigin="anonymous" media="all" rel="stylesheet" data-href="https://github.githubassets.com/assets/dark_dimmed_high_contrast_experimental-dc9a2a96cdc6.css">


    <link crossorigin="anonymous" media="all" rel="stylesheet" href="./app_files/primer-primitives-225433424a87.css">
    <link crossorigin="anonymous" media="all" rel="stylesheet" href="./app_files/primer-b4bd0459f984.css">
    <link crossorigin="anonymous" media="all" rel="stylesheet" href="./app_files/global-46e30a0a488d.css">
    <link crossorigin="anonymous" media="all" rel="stylesheet" href="./app_files/github-ef14fd9f242b.css">
  <link crossorigin="anonymous" media="all" rel="stylesheet" href="./app_files/repository-fa462f1c51f1.css">
<link crossorigin="anonymous" media="all" rel="stylesheet" href="./app_files/code-177d21388df8.css">

  


  <script type="application/json" id="client-env">{"locale":"en","featureFlags":["alternate_user_config_repo","api_insights_show_missing_data_banner","appearance_settings","billing_sku_level_budgets","client_version_header","codespaces_prebuild_region_target_update","contact_requests_implicit_opt_in","contentful_lp_flex_features","contentful_lp_footnotes","contentful_lp_form_phone_e164","copilot_chat_attach_images","copilot_chat_attach_multiple_images","copilot_chat_attachments","copilot_chat_autocomplete","copilot_chat_custom_instructions","copilot_chat_opening_thread_switch","copilot_chat_repo_custom_instructions_preview","copilot_chat_vision_in_claude","copilot_chat_wholearea_dd","copilot_custom_copilots_feature_preview","copilot_dotcom_chat_file_upload","copilot_duplicate_thread","copilot_free_to_paid_telem","copilot_ftp_settings_upgrade","copilot_ftp_upgrade_to_pro_from_models","copilot_ftp_your_copilot_settings","copilot_immersive_draft_issue_template_required","copilot_immersive_issue_creation_cta","copilot_immersive_issue_preview","copilot_new_conversation_starters","copilot_new_immersive_references_ui","copilot_no_floating_button","copilot_read_shared_conversation","copilot_share_active_subthread","copilot_showcase_icebreakers","copilot_task_oriented_assistive_prompts","copilot_topics_as_references","copilot_workbench_iterate_panel","copilot_workbench_preview_analytics","copilot_workbench_refresh_on_wsod","copilot_workbench_user_limits","custom_copilots_capi_mode","direct_to_salesforce","dnd_no_touch_device_check","dotcom_chat_client_side_skills","ghost_pilot_confidence_truncation_25","ghost_pilot_confidence_truncation_40","insert_before_patch","issues_react_blur_item_picker_on_close","issues_react_bots_timeline_pagination","issues_react_create_milestone","issues_react_include_bots_in_pickers","issues_react_prohibit_title_fallback","issues_react_remove_placeholders","lifecycle_label_name_updates","link_contact_sales_swp_marketo","marketing_pages_search_explore_provider","memex_mwl_filter_field_delimiter","memex_roadmap_drag_style","nonreporting_relay_graphql_status_codes","primer_primitives_experimental","primer_react_css_modules_ga","primer_react_select_panel_with_modern_action_list","progress_bar_delay_99","remove_child_patch","repository_suggester_elastic_search","sample_network_conn_type","sanitize_nested_mathjax_macros","site_homepage_contentful","site_msbuild_hide_integrations","site_msbuild_launch","site_msbuild_webgl_hero","spark_auth_token_endpoint","spark_commit_on_default_branch","spark_update_user_edit_status","swp_enterprise_contact_form","use_copilot_avatar","use_paginated_org_picker_cost_center_form","use_paginated_repo_picker_cost_center_form"],"login":"Jetgar"}</script>
<script crossorigin="anonymous" type="application/javascript" src="./app_files/wp-runtime-ed8567247130.js.download" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="./app_files/vendors-node_modules_oddbird_popover-polyfill_dist_popover-fn_js-a8c266e5f126.js.download" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="./app_files/vendors-node_modules_github_mini-throttle_dist_index_js-node_modules_stacktrace-parser_dist_s-1d3d52-babac9434833.js.download" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="./app_files/ui_packages_failbot_failbot_ts-25fbe4f052b4.js.download" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="./app_files/environment-89128d48c6ff.js.download" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="./app_files/vendors-node_modules_primer_behaviors_dist_esm_index_mjs-c44edfed7f0d.js.download" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="./app_files/vendors-node_modules_github_selector-observer_dist_index_esm_js-cdf2757bd188.js.download" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="./app_files/vendors-node_modules_github_relative-time-element_dist_index_js-5913bc24f35d.js.download" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="./app_files/vendors-node_modules_github_text-expander-element_dist_index_js-e50fb7a5fe8c.js.download" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="./app_files/vendors-node_modules_github_auto-complete-element_dist_index_js-node_modules_github_catalyst_-8e9f78-c1e2fb329866.js.download" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="./app_files/vendors-node_modules_github_filter-input-element_dist_index_js-node_modules_github_remote-inp-d8c643-251bc3964eb6.js.download" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="./app_files/vendors-node_modules_github_markdown-toolbar-element_dist_index_js-6a8c7d9a08fe.js.download" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="./app_files/vendors-node_modules_github_file-attachment-element_dist_index_js-node_modules_primer_view-co-cadbad-fad3eaf3c7ec.js.download" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="./app_files/github-elements-a0eacac9865b.js.download" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="./app_files/element-registry-d0efed5dc7c8.js.download" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="./app_files/vendors-node_modules_braintree_browser-detection_dist_browser-detection_js-node_modules_githu-bb80ec-34c4b68b1dd3.js.download" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="./app_files/vendors-node_modules_lit-html_lit-html_js-b93a87060d31.js.download" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="./app_files/vendors-node_modules_morphdom_dist_morphdom-esm_js-300e8e4e0414.js.download" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="./app_files/vendors-node_modules_fzy_js_index_js-node_modules_github_paste-markdown_dist_index_js-63a26702fa42.js.download" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="./app_files/vendors-node_modules_github_turbo_dist_turbo_es2017-esm_js-595819d3686f.js.download" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="./app_files/vendors-node_modules_github_remote-form_dist_index_js-node_modules_delegated-events_dist_inde-893f9f-1bcf38e06f01.js.download" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="./app_files/vendors-node_modules_color-convert_index_js-1a149db8dc99.js.download" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="./app_files/vendors-node_modules_github_quote-selection_dist_index_js-node_modules_github_session-resume_-c1aa61-91618cb63471.js.download" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="./app_files/ui_packages_updatable-content_updatable-content_ts-a5daa16ae903.js.download" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="./app_files/app_assets_modules_github_behaviors_task-list_ts-app_assets_modules_github_sso_ts-ui_packages-900dde-f953ddf42948.js.download" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="./app_files/app_assets_modules_github_sticky-scroll-into-view_ts-84e0c4a441a7.js.download" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="./app_files/app_assets_modules_github_behaviors_ajax-error_ts-app_assets_modules_github_behaviors_include-d0d0a6-a7da4270c5f4.js.download" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="./app_files/app_assets_modules_github_behaviors_commenting_edit_ts-app_assets_modules_github_behaviors_ht-83c235-567e0f340e27.js.download" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="./app_files/behaviors-b02c9c945bf2.js.download" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="./app_files/vendors-node_modules_delegated-events_dist_index_js-node_modules_github_catalyst_lib_index_js-ea8eaa-eefe25567449.js.download" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="./app_files/notifications-global-eadae94940d6.js.download" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="./app_files/vendors-node_modules_github_mini-throttle_dist_index_js-node_modules_virtualized-list_es_inde-5cfb7e-03a3356911e6.js.download" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="./app_files/vendors-node_modules_github_remote-form_dist_index_js-node_modules_delegated-events_dist_inde-70450e-bd02070d35a3.js.download" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="./app_files/app_assets_modules_github_ref-selector_ts-8b8b0f9b4d26.js.download" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="./app_files/codespaces-beb77f9a88fd.js.download" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="./app_files/vendors-node_modules_github_filter-input-element_dist_index_js-node_modules_github_remote-inp-3eebbd-c8d976843cc9.js.download" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="./app_files/vendors-node_modules_github_mini-throttle_dist_decorators_js-node_modules_delegated-events_di-e161aa-7cb68a617c15.js.download" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="./app_files/vendors-node_modules_github_file-attachment-element_dist_index_js-node_modules_github_remote--3c9c82-aa5ff674466d.js.download" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="./app_files/repositories-853f2e9a1ebb.js.download" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="./app_files/vendors-node_modules_github_mini-throttle_dist_index_js-node_modules_github_catalyst_lib_inde-dbbea9-558c1f223d1d.js.download" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="./app_files/code-menu-6d3334d79340.js.download" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="./app_files/primer-react-957709c85fcc.js.download" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="./app_files/react-core-577edb5c37f8.js.download" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="./app_files/react-lib-8705026b409a.js.download" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="./app_files/octicons-react-9fd6ca6872cc.js.download" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="./app_files/vendors-node_modules_emotion_is-prop-valid_dist_emotion-is-prop-valid_esm_js-node_modules_emo-b1c483-b5947865157f.js.download" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="./app_files/vendors-ui_packages_react-router_node_modules_cookie_dist_index_js-node_modules_primer_live-r-4288ca-b9012d3355e6.js.download" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="./app_files/vendors-node_modules_tanstack_query-core_build_modern_queryObserver_js-node_modules_tanstack_-defd52-0024bc0658ed.js.download" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="./app_files/ui_packages_agent-sessions_utils_elapsed-time-util_ts-ui_packages_agent-sessions_hooks_useSes-bd1a31-05ef3f30f012.js.download" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="./app_files/copilot-coding-agent-status-053fc52903d2.js.download" defer="defer"></script>
<link crossorigin="anonymous" media="all" rel="stylesheet" href="./app_files/primer-react.c212c596cc6bbefb1798.module.css">
<link crossorigin="anonymous" media="all" rel="stylesheet" href="./app_files/copilot-coding-agent-status.32796c3e0ecdbdaa8ce6.module.css">
  
  <link crossorigin="anonymous" media="all" rel="stylesheet" href="./app_files/notifications-subscriptions-menu.e5e6e593370c808590a5.module.css">


  



  
  
  
  

    
  


  


    


  
  

  
  

    



  

  




    

  

    

    

      

      

    
    
    

      
  
  


      
      


      


      
      
      

        


  <meta http-equiv="x-pjax-version" content="4671293dff3f592e3319b65c7fc797aee10efa385d74a64706a830a5d5848b90" data-turbo-track="reload">
  <meta http-equiv="x-pjax-csp-version" content="352e51c42d5f5727a7c545752bf34d1f83f40219e7036c6959817149a51651bc" data-turbo-track="reload">
  <meta http-equiv="x-pjax-css-version" content="4e8d942c1e58aee61c7c4c8c9889c1c76351814c062c507d76d301fb8bcb7735" data-turbo-track="reload">
  <meta http-equiv="x-pjax-js-version" content="42da424b19d541f486772b732f7df5c31a35a38b9cc22cb9806f986ba9ba67e0" data-turbo-track="reload">

  

      
  

  



      


    


  

  

  

  
  
  




  
  

  

  <style data-styled="active" data-styled-version="5.3.11"></style><style id="ms-consent-banner-main-styles">.w8hcgFksdo30C8w-bygqu{color:#000}.ydkKdaztSS0AeHWIeIHsQ a{color:#0067B8}.erL690_8JwUW-R4bJRcfl{background-color:#EBEBEB;border:none;color:#000}.erL690_8JwUW-R4bJRcfl:enabled:hover{color:#000;background-color:#DBDBDB;box-shadow:0px 4px 10px rgba(0,0,0,0.25);border:none}.erL690_8JwUW-R4bJRcfl:enabled:focus{background-color:#DBDBDB;box-shadow:0px 4px 10px rgba(0,0,0,0.25);border:2px solid #000}.erL690_8JwUW-R4bJRcfl:disabled{opacity:1;color:rgba(0,0,0,0.2);background-color:rgba(0,0,0,0.2);border:none}._1zNQOqxpBFSokeCLGi_hGr{border:none;background-color:#0067B8;color:#fff}._1zNQOqxpBFSokeCLGi_hGr:enabled:hover{color:#fff;background-color:#0067B8;box-shadow:0px 4px 10px rgba(0,0,0,0.25);border:none}._1zNQOqxpBFSokeCLGi_hGr:enabled:focus{background-color:#0067B8;box-shadow:0px 4px 10px rgba(0,0,0,0.25);border:2px solid #000}._1zNQOqxpBFSokeCLGi_hGr:disabled{opacity:1;color:rgba(0,0,0,0.2);background-color:rgba(0,120,215,0.2);border:none}._23tra1HsiiP6cT-Cka-ycB{position:relative;display:flex;z-index:9999;width:100%;background-color:#F2F2F2;justify-content:space-between;text-align:left}div[dir="rtl"]._23tra1HsiiP6cT-Cka-ycB{text-align:right}._1Upc2NjY8AlDn177YoVj0y{margin:0;padding-left:5%;padding-top:8px;padding-bottom:8px}div[dir="rtl"] ._1Upc2NjY8AlDn177YoVj0y{margin:0;padding:8px 5% 8px 0;float:none}._23tra1HsiiP6cT-Cka-ycB svg{fill:none;max-width:none;max-height:none}._1V_hlU-7jdtPiooHMu89BB{display:table-cell;padding:12px;width:24px;height:24px;font-family:Segoe UI, SegoeUI, Arial, sans-serif;font-style:normal;font-weight:normal;font-size:24px;line-height:0}.f6QKJD7fhSbnJLarTL-W-{display:table-cell;vertical-align:middle;padding:0;font-family:Segoe UI, SegoeUI, Arial, sans-serif;font-style:normal;font-weight:normal;font-size:13px;line-height:16px}.f6QKJD7fhSbnJLarTL-W- a{text-decoration:underline}._2j0fmugLb1FgYz6KPuB91w{display:inline-block;margin-left:5%;margin-right:5%;min-width:40%;min-width:calc((150px + 3 * 4px) * 2 + 150px);min-width:-webkit-fit-content;min-width:-moz-fit-content;min-width:fit-content;align-self:center;position:relative}._1XuCi2WhiqeWRUVp3pnFG3{margin:4px;padding:5px;min-width:150px;min-height:36px;vertical-align:top;cursor:pointer;font-family:Segoe UI, SegoeUI, Arial, sans-serif;font-style:normal;font-weight:normal;font-size:15px;line-height:20px;text-align:center}._1XuCi2WhiqeWRUVp3pnFG3:focus{box-sizing:border-box}._1XuCi2WhiqeWRUVp3pnFG3:disabled{cursor:not-allowed}._2bvsb3ubApyZ0UGoQA9O9T{display:block;position:fixed;z-index:10000;top:0;left:0;width:100%;height:100%;background-color:rgba(255,255,255,0.6);overflow:auto;text-align:left}div[dir="rtl"]._2bvsb3ubApyZ0UGoQA9O9T{text-align:right}div[dir="rtl"] ._2bvsb3ubApyZ0UGoQA9O9T{left:auto;right:0}.AFsJE948muYyzCMktdzuk{position:relative;top:8%;margin-bottom:40px;margin-left:auto;margin-right:auto;box-sizing:border-box;width:640px;background-color:#fff;border:1px solid #0067B8}._3kWyBRbW_dgnMiEyx06Fu4{float:right;z-index:1;margin:2px;padding:12px;border:none;cursor:pointer;font-family:Segoe UI, SegoeUI, Arial, sans-serif;font-style:normal;font-weight:normal;font-size:13px;line-height:13px;display:flex;align-items:center;text-align:center;color:#666;background-color:#fff}div[dir="rtl"] ._3kWyBRbW_dgnMiEyx06Fu4{margin:2px;padding:12px;float:left}.uCYvKvHXrhjNgflv1VqdD{position:static;margin-top:36px;margin-left:36px;margin-right:36px}._17pX1m9O_W--iZbDt3Ta5r{margin-top:0;margin-bottom:12px;font-family:Segoe UI, SegoeUI, Arial, sans-serif;font-style:normal;font-weight:600;font-size:20px;line-height:24px;text-transform:none}._1kBkHQ1V1wu3kl-YcLgUr6{height:446px;overflow:auto}._20_nXDf6uFs9Q6wxRXG-I-{margin-top:0;font-family:Segoe UI, SegoeUI, Arial, sans-serif;font-style:normal;font-weight:normal;font-size:15px;line-height:20px}._20_nXDf6uFs9Q6wxRXG-I- a{text-decoration:underline}dl._2a0NH_GDQEQe5Ynfo7suVH{margin-top:36px;margin-bottom:0;padding:0;list-style:none;text-transform:none}dt._3j_LCPv7fyXv3A8FIXVwZ4{margin-top:20px;float:none;font-family:Segoe UI, SegoeUI, Arial, sans-serif;font-style:normal;font-weight:600;font-size:18px;line-height:24px;list-style:none}.k-vxTGFbdq1aOZB2HHpjh{margin:0;padding:0;border:none}._2Bucyy75c_ogoU1g-liB5R{margin:0;padding:0;border-bottom:none;font-family:Segoe UI, SegoeUI, Arial, sans-serif;font-style:normal;font-weight:600;font-size:18px;line-height:24px;text-transform:none}._63gwfzV8dclrsl2cfd90r{display:inline-block;margin-top:0;margin-bottom:13px;font-family:Segoe UI, SegoeUI, Arial, sans-serif;font-style:normal;font-weight:normal;font-size:15px;line-height:20px}._1l8wM_4mRYGz3Iu7l3BZR7{display:block}._2UE03QS02aZGkslegN_F-i{display:inline-block;position:relative;left:5px;margin-bottom:13px;margin-right:34px;padding:3px}div[dir="rtl"] ._2UE03QS02aZGkslegN_F-i{margin:0 0 13px 34px;padding:3px;float:none}div[dir="rtl"] ._2UE03QS02aZGkslegN_F-i{left:auto;right:5px}._23tra1HsiiP6cT-Cka-ycB *::before,._2bvsb3ubApyZ0UGoQA9O9T *::before,._23tra1HsiiP6cT-Cka-ycB *::after,._2bvsb3ubApyZ0UGoQA9O9T *::after{box-sizing:inherit}._1HSFn0HzGo6w4ADApV8-c4{outline:2px solid rgba(0,0,0,0.8)}input[type="radio"]._1dp8Vp5m3HwAqGx8qBmFV2{display:inline-block;position:relative;margin-top:0;margin-left:0;margin-right:0;height:0;width:0;border-radius:0;cursor:pointer;outline:none;box-sizing:border-box;-webkit-appearance:none;-moz-appearance:none;appearance:none}input[type="radio"]._1dp8Vp5m3HwAqGx8qBmFV2+label::before{display:block;position:absolute;top:5px;left:3px;height:19px;width:19px;content:"";border-radius:50%;border:1px solid #000;background-color:#fff}div[dir="rtl"] input[type="radio"]._1dp8Vp5m3HwAqGx8qBmFV2+label::before{left:auto;right:3px}input[type="radio"]._1dp8Vp5m3HwAqGx8qBmFV2:not(:disabled)+label:hover::before{border:1px solid #0067B8}input[type="radio"]._1dp8Vp5m3HwAqGx8qBmFV2:not(:disabled)+label:hover::after{display:block;position:absolute;top:10px;left:8px;height:9px;width:9px;content:"";border-radius:50%;background-color:rgba(0,0,0,0.8)}div[dir="rtl"] input[type="radio"]._1dp8Vp5m3HwAqGx8qBmFV2:not(:disabled)+label:hover::after{left:auto;right:8px}input[type="radio"]._1dp8Vp5m3HwAqGx8qBmFV2:not(:disabled)+label:focus::before{border:1px solid #0067B8}input[type="radio"]._1dp8Vp5m3HwAqGx8qBmFV2:not(:disabled)+label:focus::after{display:block;position:absolute;top:10px;left:8px;height:9px;width:9px;content:"";border-radius:50%;background-color:#000}div[dir="rtl"] input[type="radio"]._1dp8Vp5m3HwAqGx8qBmFV2:not(:disabled)+label:focus::after{left:auto;right:8px}input[type="radio"]._1dp8Vp5m3HwAqGx8qBmFV2:checked+label::after{display:block;position:absolute;top:10px;left:8px;height:9px;width:9px;content:"";border-radius:50%;background-color:#000}div[dir="rtl"] input[type="radio"]._1dp8Vp5m3HwAqGx8qBmFV2:checked+label::after{left:auto;right:8px}input[type="radio"]._1dp8Vp5m3HwAqGx8qBmFV2:disabled+label{cursor:not-allowed}input[type="radio"]._1dp8Vp5m3HwAqGx8qBmFV2:disabled+label::before{border:1px solid rgba(0,0,0,0.2);background-color:rgba(0,0,0,0.2)}._3RJzeL3l9Rl_lAQEm6VwdX{display:block;position:static;float:right;margin-top:0;margin-bottom:0;margin-left:19px;margin-right:0;padding-top:0;padding-bottom:0;padding-left:8px;padding-right:0;width:80%;width:calc(100% - 19px);font-family:Segoe UI, SegoeUI, Arial, sans-serif;font-style:normal;font-weight:normal;font-size:15px;line-height:20px;text-transform:none;cursor:pointer;box-sizing:border-box}div[dir="rtl"] ._3RJzeL3l9Rl_lAQEm6VwdX{margin:0 19px 0 0;padding:0 8px 0 0;float:left}.nohp3sIG12ZBhzcMnPala{margin-top:20px;margin-bottom:48px}._2uhaEsmeotZ3P-M0AXo2kF{padding:0;width:278px;height:36px;cursor:pointer;font-family:Segoe UI, SegoeUI, Arial, sans-serif;font-style:normal;font-weight:normal;font-size:15px;line-height:20px;text-align:center}._2uhaEsmeotZ3P-M0AXo2kF:focus{box-sizing:border-box}._2uhaEsmeotZ3P-M0AXo2kF:disabled{cursor:not-allowed}._3tOu1FJ59c_xz_PmI1lKV5{float:right;padding:0;width:278px;height:36px;cursor:pointer;font-family:Segoe UI, SegoeUI, Arial, sans-serif;font-style:normal;font-weight:normal;font-size:15px;line-height:20px;text-align:center}._3tOu1FJ59c_xz_PmI1lKV5:focus{box-sizing:border-box}._3tOu1FJ59c_xz_PmI1lKV5:disabled{cursor:not-allowed}div[dir="rtl"] ._3tOu1FJ59c_xz_PmI1lKV5{margin:0;padding:0;float:left}@media only screen and (max-width: 768px){._2j0fmugLb1FgYz6KPuB91w,._1Upc2NjY8AlDn177YoVj0y{padding-top:8px;padding-bottom:12px;padding-left:3.75%;padding-right:3.75%;margin:0;width:92.5%}._23tra1HsiiP6cT-Cka-ycB{display:block}._1XuCi2WhiqeWRUVp3pnFG3{margin-bottom:8px;margin-left:0;margin-right:0;width:100%}._2bvsb3ubApyZ0UGoQA9O9T{overflow:hidden}.AFsJE948muYyzCMktdzuk{top:1.8%;width:93.33%;height:96.4%;overflow:hidden}.uCYvKvHXrhjNgflv1VqdD{margin-top:24px;margin-left:24px;margin-right:24px;height:100%}._1kBkHQ1V1wu3kl-YcLgUr6{height:62%;height:calc(100% - 188px);min-height:50%}._2uhaEsmeotZ3P-M0AXo2kF{width:100%}._3tOu1FJ59c_xz_PmI1lKV5{margin-bottom:12px;margin-left:0;width:100%}div[dir="rtl"] ._3tOu1FJ59c_xz_PmI1lKV5{margin:0 0 12px 0;padding:0;float:none}}@media only screen and (max-width: 768px) and (orientation: landscape), only screen and (max-height: 260px), only screen and (max-width: 340px){.AFsJE948muYyzCMktdzuk{overflow:auto}}@media only screen and (max-height: 260px), only screen and (max-width: 340px){._1XuCi2WhiqeWRUVp3pnFG3{min-width:0}._3kWyBRbW_dgnMiEyx06Fu4{padding:3%}.uCYvKvHXrhjNgflv1VqdD{margin-top:3%;margin-left:3%;margin-right:3%}._17pX1m9O_W--iZbDt3Ta5r{margin-bottom:3%}._1kBkHQ1V1wu3kl-YcLgUr6{height:calc(79% - 64px)}.nohp3sIG12ZBhzcMnPala{margin-top:5%;margin-bottom:10%}._3tOu1FJ59c_xz_PmI1lKV5{margin-bottom:3%}div[dir="rtl"] ._3tOu1FJ59c_xz_PmI1lKV5{margin:0 0 3% 0;padding:0;float:none}}
</style><style type="text/css" id="ms-consent-banner-theme-styles">._23tra1HsiiP6cT-Cka-ycB {
            background-color: #24292f !important;
        }.w8hcgFksdo30C8w-bygqu {
            color: #ffffff !important;
        }.ydkKdaztSS0AeHWIeIHsQ a {
            color: #d8b9ff !important;
        }._2bvsb3ubApyZ0UGoQA9O9T {
            background-color: rgba(23, 23, 23, 0.8) !important;
        }.AFsJE948muYyzCMktdzuk {
            background-color: #24292f !important;
            border: 1px solid #d8b9ff !important;
        }._3kWyBRbW_dgnMiEyx06Fu4 {
            color: #d8b9ff !important;
            background-color: #24292f !important;
        }._1zNQOqxpBFSokeCLGi_hGr {
            border: 1px solid #ffffff !important;
            background-color: #ffffff !important;
            color: #1f2328 !important;
        }._1zNQOqxpBFSokeCLGi_hGr:enabled:hover {
            color: #1f2328 !important;
            background-color: #d8b9ff !important;
            box-shadow: none !important;
            border: 1px solid transparent !important;
        }._1zNQOqxpBFSokeCLGi_hGr:enabled:focus {
            background-color: #d8b9ff !important;
            box-shadow: none !important;
            border: 2px solid #ffffff !important;
        }._1zNQOqxpBFSokeCLGi_hGr:disabled {
            opacity: 0.5 !important;
            color: #1f2328 !important;
            background-color: #ffffff !important;
            border: 1px solid transparent !important;
        }.erL690_8JwUW-R4bJRcfl {
            border: 1px solid #eaeef2 !important;
            background-color: #32383f !important;
            color: #ffffff !important;
        }.erL690_8JwUW-R4bJRcfl:enabled:hover {
            color: #ffffff !important;
            background-color: #24292f !important;
            box-shadow: none !important;
            border: 1px solid #ffffff !important;
        }.erL690_8JwUW-R4bJRcfl:enabled:focus {
            background-color: #24292f !important;
            box-shadow: none !important;
            border: 2px solid #6e7781 !important;
        }.erL690_8JwUW-R4bJRcfl:disabled {
            opacity: 0.5 !important;
            color: #ffffff !important;
            background-color: #424a53 !important;
            border: 1px solid #6e7781 !important;
        }input[type="radio"]._1dp8Vp5m3HwAqGx8qBmFV2 + label::before {
            border: 1px solid #d8b9ff !important;
            background-color: #24292f !important;
        }._1HSFn0HzGo6w4ADApV8-c4 {
            outline: 2px solid #ffffff !important;
        }input[type="radio"]._1dp8Vp5m3HwAqGx8qBmFV2:checked + label::after {
            background-color: #d8b9ff !important;
        }input[type="radio"]._1dp8Vp5m3HwAqGx8qBmFV2 + label:hover::before {
            border: 1px solid #ffffff !important;
        }input[type="radio"]._1dp8Vp5m3HwAqGx8qBmFV2 + label:hover::after {
            background-color: #ffffff !important;
        }input[type="radio"]._1dp8Vp5m3HwAqGx8qBmFV2 + label:focus::before {
            border: 1px solid #ffffff !important;
        }input[type="radio"]._1dp8Vp5m3HwAqGx8qBmFV2 + label:focus::after {
            background-color: #d8b9ff !important;
        }input[type="radio"]._1dp8Vp5m3HwAqGx8qBmFV2:disabled + label::before {
            border: 1px solid rgba(227, 227, 227, 0.2) !important;
            background-color: rgba(227, 227, 227, 0.2) !important;
        }</style><link rel="stylesheet" type="text/css" href="./app_files/ui_packages_code-view-shared_components_files-search_FileResultsList_tsx.b824b197dc91fa971d59.module.css" crossorigin="anonymous"><link crossorigin="anonymous" media="all" rel="stylesheet" href="./app_files/react-code-view.f828e7c17d2129f3c506.module.css"><script crossorigin="anonymous" type="application/javascript" src="./app_files/vendors-node_modules_dompurify_dist_purify_es_mjs-7457ebdd1a1f.js.download" defer="defer"></script><script crossorigin="anonymous" type="application/javascript" src="./app_files/vendors-node_modules_lodash-es__Stack_js-node_modules_lodash-es__Uint8Array_js-node_modules_l-4faaa6-16c4e2c524de.js.download" defer="defer"></script><script crossorigin="anonymous" type="application/javascript" src="./app_files/vendors-node_modules_lodash-es_isEqual_js-a0841ced23fc.js.download" defer="defer"></script><script crossorigin="anonymous" type="application/javascript" src="./app_files/vendors-node_modules_tanstack_react-virtual_dist_esm_index_js-807aab04afeb.js.download" defer="defer"></script><script crossorigin="anonymous" type="application/javascript" src="./app_files/vendors-node_modules_github_catalyst_lib_index_js-node_modules_github_hydro-analytics-client_-189aa3-aa0d1c491a18.js.download" defer="defer"></script><script crossorigin="anonymous" type="application/javascript" src="./app_files/vendors-node_modules_focus-visible_dist_focus-visible_js-node_modules_fzy_js_index_js-node_mo-296806-a0e432a5dd85.js.download" defer="defer"></script><script crossorigin="anonymous" type="application/javascript" src="./app_files/ui_packages_document-metadata_document-metadata_ts-ui_packages_history_history_ts-ui_packages-417c81-00e1a3522739.js.download" defer="defer"></script><script crossorigin="anonymous" type="application/javascript" src="./app_files/ui_packages_paths_index_ts-2c6108a4a75d.js.download" defer="defer"></script><script crossorigin="anonymous" type="application/javascript" src="./app_files/ui_packages_ref-selector_RefSelector_tsx-2403bac2539f.js.download" defer="defer"></script><script crossorigin="anonymous" type="application/javascript" src="./app_files/ui_packages_commit-attribution_index_ts-ui_packages_commit-checks-status_index_ts-ui_packages-762eaa-0e1369379126.js.download" defer="defer"></script><script crossorigin="anonymous" type="application/javascript" src="./app_files/ui_packages_app-uuid_app-uuid_ts-ui_packages_repos-file-tree-view_repos-file-tree-view_ts-ui_-e7c631-8808400bf5af.js.download" defer="defer"></script><script crossorigin="anonymous" type="application/javascript" src="./app_files/ui_packages_diffs_diff-parts_ts-3d204ed86299.js.download" defer="defer"></script><script crossorigin="anonymous" type="application/javascript" src="./app_files/ui_packages_hydro-analytics_hydro-analytics_ts-ui_packages_use-client-value_use-client-value_-6f712e-5abe20edbfb5.js.download" defer="defer"></script><script crossorigin="anonymous" type="application/javascript" src="./app_files/ui_packages_code-view-shared_hooks_use-canonical-object_ts-ui_packages_code-view-shared_hooks-7b64b1-b9ed65eb20ca.js.download" defer="defer"></script><script crossorigin="anonymous" type="application/javascript" src="./app_files/app_assets_modules_github_blob-anchor_ts-ui_packages_code-nav_code-nav_ts-ui_packages_filter--8253c1-5fde020dbad1.js.download" defer="defer"></script><script crossorigin="anonymous" type="application/javascript" src="./app_files/react-code-view-d2179f9d5494.js.download" defer="defer"></script><link rel="dns-prefetch" href="https://github.githubassets.com/"><link rel="dns-prefetch" href="https://avatars.githubusercontent.com/"><link rel="dns-prefetch" href="https://github-cloud.s3.amazonaws.com/"><link rel="dns-prefetch" href="https://user-images.githubusercontent.com/"><link rel="preconnect" href="https://github.githubassets.com/" crossorigin=""><link rel="preconnect" href="https://avatars.githubusercontent.com/"><title>-Deploy_ke_Streamlit_Cloud/app.py at main · fastabyq/-Deploy_ke_Streamlit_Cloud</title><meta name="route-pattern" content="/:user_id/:repository/blob/*name(/*path)" data-turbo-transient=""><meta name="route-controller" content="blob" data-turbo-transient=""><meta name="route-action" content="show" data-turbo-transient=""><meta name="fetch-nonce" content="v2:fac17c6a-5a3e-3145-7e99-dbeb3ad3f493"><meta name="current-catalog-service-hash" content="f3abb0cc802f3d7b95fc8762b94bdcb13bf39634c40c357301c4aa1d67a256fb"><meta name="request-id" content="F92C:3FEB92:13BCD:15E64:684FD6FA" data-turbo-transient="true"><meta name="html-safe-nonce" content="0dd086e7440e17cd5f84e0bf3685352db60b21428ced5002d438465bd43e8f8c" data-turbo-transient="true"><meta name="visitor-payload" content="eyJyZWZlcnJlciI6Imh0dHBzOi8vZ2l0aHViLmNvbS9mYXN0YWJ5cS8tRGVwbG95X2tlX1N0cmVhbWxpdF9DbG91ZC9ibG9iL21haW4vYXBwLnB5IiwicmVxdWVzdF9pZCI6IkY5MkM6M0ZFQjkyOjEzQkNEOjE1RTY0OjY4NEZENkZBIiwidmlzaXRvcl9pZCI6IjI2MjY3MzAyNDgyNTQ4MTMxNzEiLCJyZWdpb25fZWRnZSI6InNvdXRoZWFzdGFzaWEiLCJyZWdpb25fcmVuZGVyIjoiaWFkIn0=" data-turbo-transient="true"><meta name="visitor-hmac" content="095894d3ae367035eefaa9d4ea4750430aa086e937171c1860bf870cbc3b83a3" data-turbo-transient="true"><meta name="hovercard-subject-tag" content="repository:994512716" data-turbo-transient=""><meta name="github-keyboard-shortcuts" content="repository,source-code,file-tree,copilot" data-turbo-transient="true"><meta name="selected-link" value="repo_source" data-turbo-transient=""><link rel="assets" href="https://github.githubassets.com/"><meta name="google-site-verification" content="Apib7-x98H0j5cPqHWwSMm6dNU4GmODRoqxLiDzdx9I"><meta name="octolytics-url" content="https://collector.github.com/github/collect"><meta name="octolytics-actor-id" content="128130347"><meta name="octolytics-actor-login" content="Jetgar"><meta name="octolytics-actor-hash" content="2ba91fa7fa0010737bbd66bd62642f6a7df28d80af388dfe192ac5f4f99924e0"><meta name="analytics-location" content="/&lt;user-name&gt;/&lt;repo-name&gt;/blob/show" data-turbo-transient="true"><meta name="user-login" content="Jetgar"><link rel="sudo-modal" href="https://github.com/sessions/sudo_modal"><meta name="turbo-cache-control" content="no-preview" data-turbo-transient=""><meta name="turbo-cache-control" content="no-cache" data-turbo-transient=""><meta data-hydrostats="publish"><meta name="go-import" content="github.com/fastabyq/-Deploy_ke_Streamlit_Cloud git https://github.com/fastabyq/-Deploy_ke_Streamlit_Cloud.git"><meta name="octolytics-dimension-user_id" content="171785532"><meta name="octolytics-dimension-user_login" content="fastabyq"><meta name="octolytics-dimension-repository_id" content="994512716"><meta name="octolytics-dimension-repository_nwo" content="fastabyq/-Deploy_ke_Streamlit_Cloud"><meta name="octolytics-dimension-repository_public" content="true"><meta name="octolytics-dimension-repository_is_fork" content="false"><meta name="octolytics-dimension-repository_network_root_id" content="994512716"><meta name="octolytics-dimension-repository_network_root_nwo" content="fastabyq/-Deploy_ke_Streamlit_Cloud"><meta name="turbo-body-classes" content="logged-in env-production page-responsive"><meta name="browser-stats-url" content="https://api.github.com/_private/browser/stats"><meta name="browser-errors-url" content="https://api.github.com/_private/browser/errors"><meta name="release" content="93b6ffc34ad4e0cb15e2fd4aef917ac73def97e2"><link rel="mask-icon" href="https://github.githubassets.com/assets/pinned-octocat-093da3e6fa40.svg" color="#000000"><link rel="alternate icon" class="js-site-favicon" type="image/png" href="https://github.githubassets.com/favicons/favicon-dark.png"><link rel="icon" class="js-site-favicon" type="image/svg+xml" href="https://github.githubassets.com/favicons/favicon-dark.svg" data-base-href="https://github.githubassets.com/favicons/favicon"><meta name="theme-color" content="#1e2327"><meta name="color-scheme" content="light dark"><meta name="msapplication-TileImage" content="/windows-tile.png"><meta name="msapplication-TileColor" content="#ffffff"><link rel="manifest" href="https://github.com/manifest.json" crossorigin="use-credentials"><style type="text/css" id="ms-consent-banner-theme-styles"></style></head>

  <body class="logged-in env-production page-responsive" style="overflow-wrap: break-word; --dialog-scrollgutter: 15px;">
    <div data-turbo-body="" class="logged-in env-production page-responsive" style="word-wrap: break-word;">
      



    <div class="position-relative header-wrapper js-header-wrapper ">
      <a href="https://github.com/fastabyq/-Deploy_ke_Streamlit_Cloud/blob/main/app.py#start-of-content" data-skip-target-assigned="false" class="p-3 color-bg-accent-emphasis color-fg-on-emphasis show-on-focus js-skip-to-content">Skip to content</a>

      <span data-view-component="true" class="progress-pjax-loader Progress position-fixed width-full">
    <span style="width: 0%;" data-view-component="true" class="Progress-item progress-pjax-loader-bar left-0 top-0 color-bg-accent-emphasis"></span>
</span>      
      
      <script crossorigin="anonymous" type="application/javascript" src="./app_files/ui_packages_ui-commands_ui-commands_ts-eb77c4447210.js.download" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="./app_files/keyboard-shortcuts-dialog-693d9bb9de03.js.download" defer="defer"></script>
<link crossorigin="anonymous" media="all" rel="stylesheet" href="./app_files/primer-react.c212c596cc6bbefb1798.module.css">
<link crossorigin="anonymous" media="all" rel="stylesheet" href="./app_files/keyboard-shortcuts-dialog.47de85e2c17af43cefd5.module.css">

<react-partial partial-name="keyboard-shortcuts-dialog" data-ssr="false" data-attempted-ssr="false" data-react-profiling="false" data-catalyst="" class="loaded">
  
  <script type="application/json" data-target="react-partial.embeddedData">{"props":{"docsUrl":"https://docs.github.com/get-started/accessibility/keyboard-shortcuts"}}</script>
  <div data-target="react-partial.reactRoot"><div class="d-none"></div><script type="application/json" id="__PRIMER_DATA_:rv:__">{"resolvedServerColorMode":"night"}</script></div>
</react-partial>




      

          

              <header class="AppHeader" role="banner">
  <h2 class="sr-only">Navigation Menu</h2>


    

    <div class="AppHeader-globalBar pb-2 js-global-bar">
      <div class="AppHeader-globalBar-start responsive-context-region">
        <div class="">
            <deferred-side-panel data-url="/_side-panels/global" data-catalyst="">
  <include-fragment data-target="deferred-side-panel.fragment" data-nonce="v2:fac17c6a-5a3e-3145-7e99-dbeb3ad3f493" data-view-component="true"><template shadowrootmode="open"><style>:host {display: block;}</style><slot></slot></template>
  
      <button aria-label="Open global navigation menu" data-action="click:deferred-side-panel#loadPanel click:deferred-side-panel#panelOpened" data-show-dialog-id="dialog-55d3f133-de3f-46d9-964b-466afb2de3c5" id="dialog-show-dialog-55d3f133-de3f-46d9-964b-466afb2de3c5" type="button" data-view-component="true" class="Button Button--iconOnly Button--secondary Button--medium AppHeader-button p-0 color-fg-muted">  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-three-bars Button-visual">
    <path d="M1 2.75A.75.75 0 0 1 1.75 2h12.5a.75.75 0 0 1 0 1.5H1.75A.75.75 0 0 1 1 2.75Zm0 5A.75.75 0 0 1 1.75 7h12.5a.75.75 0 0 1 0 1.5H1.75A.75.75 0 0 1 1 7.75ZM1.75 12h12.5a.75.75 0 0 1 0 1.5H1.75a.75.75 0 0 1 0-1.5Z"></path>
</svg>
</button>

<dialog-helper>
  <dialog data-target="deferred-side-panel.panel" id="dialog-55d3f133-de3f-46d9-964b-466afb2de3c5" aria-modal="true" aria-labelledby="dialog-55d3f133-de3f-46d9-964b-466afb2de3c5-title" aria-describedby="dialog-55d3f133-de3f-46d9-964b-466afb2de3c5-description" data-view-component="true" class="Overlay Overlay-whenNarrow Overlay--size-small-portrait Overlay--motion-scaleFade Overlay--placement-left SidePanel Overlay--disableScroll">
    <div styles="flex-direction: row;" data-view-component="true" class="Overlay-header">
  <div class="Overlay-headerContentWrap">
    <div class="Overlay-titleWrap">
      <h1 class="Overlay-title sr-only" id="dialog-55d3f133-de3f-46d9-964b-466afb2de3c5-title">
        Global navigation
      </h1>
            <div data-view-component="true" class="d-flex">
      <div data-view-component="true" class="AppHeader-logo position-relative">
        <svg aria-hidden="true" height="24" viewBox="0 0 24 24" version="1.1" width="24" data-view-component="true" class="octicon octicon-mark-github">
    <path d="M12 1C5.9225 1 1 5.9225 1 12C1 16.8675 4.14875 20.9787 8.52125 22.4362C9.07125 22.5325 9.2775 22.2025 9.2775 21.9137C9.2775 21.6525 9.26375 20.7862 9.26375 19.865C6.5 20.3737 5.785 19.1912 5.565 18.5725C5.44125 18.2562 4.905 17.28 4.4375 17.0187C4.0525 16.8125 3.5025 16.3037 4.42375 16.29C5.29 16.2762 5.90875 17.0875 6.115 17.4175C7.105 19.0812 8.68625 18.6137 9.31875 18.325C9.415 17.61 9.70375 17.1287 10.02 16.8537C7.5725 16.5787 5.015 15.63 5.015 11.4225C5.015 10.2262 5.44125 9.23625 6.1425 8.46625C6.0325 8.19125 5.6475 7.06375 6.2525 5.55125C6.2525 5.55125 7.17375 5.2625 9.2775 6.67875C10.1575 6.43125 11.0925 6.3075 12.0275 6.3075C12.9625 6.3075 13.8975 6.43125 14.7775 6.67875C16.8813 5.24875 17.8025 5.55125 17.8025 5.55125C18.4075 7.06375 18.0225 8.19125 17.9125 8.46625C18.6138 9.23625 19.04 10.2125 19.04 11.4225C19.04 15.6437 16.4688 16.5787 14.0213 16.8537C14.42 17.1975 14.7638 17.8575 14.7638 18.8887C14.7638 20.36 14.75 21.5425 14.75 21.9137C14.75 22.2025 14.9563 22.5462 15.5063 22.4362C19.8513 20.9787 23 16.8537 23 12C23 5.9225 18.0775 1 12 1Z"></path>
</svg>
</div></div>
    </div>
    <div class="Overlay-actionWrap">
      <button data-close-dialog-id="dialog-55d3f133-de3f-46d9-964b-466afb2de3c5" aria-label="Close" type="button" data-view-component="true" class="close-button Overlay-closeButton"><svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-x">
    <path d="M3.72 3.72a.75.75 0 0 1 1.06 0L8 6.94l3.22-3.22a.749.749 0 0 1 1.275.326.749.749 0 0 1-.215.734L9.06 8l3.22 3.22a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215L8 9.06l-3.22 3.22a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042L6.94 8 3.72 4.78a.75.75 0 0 1 0-1.06Z"></path>
</svg></button>
    </div>
  </div>
  
</div>
      <scrollable-region data-labelled-by="dialog-55d3f133-de3f-46d9-964b-466afb2de3c5-title" data-catalyst="" style="overflow: auto;">
        <div data-view-component="true" class="Overlay-body d-flex flex-column px-2">    <div data-view-component="true" class="d-flex flex-column mb-3">
        <nav aria-label="Site navigation" data-view-component="true" class="ActionList">
  
  <nav-list data-catalyst="">
    <ul data-target="nav-list.topLevelList" data-view-component="true" class="ActionListWrap">
        
          
<li data-item-id="" data-targets="nav-list.items" data-view-component="true" class="ActionListItem">
    
    
    <a data-hotkey="g d" data-analytics-event="{&quot;category&quot;:&quot;Global navigation&quot;,&quot;action&quot;:&quot;HOME&quot;,&quot;label&quot;:null}" id="item-5a2215cf-9816-4400-8e0f-ddcffd5d222c" href="https://github.com/dashboard" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-home">
    <path d="M6.906.664a1.749 1.749 0 0 1 2.187 0l5.25 4.2c.415.332.657.835.657 1.367v7.019A1.75 1.75 0 0 1 13.25 15h-3.5a.75.75 0 0 1-.75-.75V9H7v5.25a.75.75 0 0 1-.75.75h-3.5A1.75 1.75 0 0 1 1 13.25V6.23c0-.531.242-1.034.657-1.366l5.25-4.2Zm1.25 1.171a.25.25 0 0 0-.312 0l-5.25 4.2a.25.25 0 0 0-.094.196v7.019c0 .138.112.25.25.25H5.5V8.25a.75.75 0 0 1 .75-.75h3.5a.75.75 0 0 1 .75.75v5.25h2.75a.25.25 0 0 0 .25-.25V6.23a.25.25 0 0 0-.094-.195Z"></path>
</svg>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
          Home
</span>      
</a>
  
</li>

        
          
<li data-item-id="" data-targets="nav-list.items" data-view-component="true" class="ActionListItem">
    
    
    <a data-hotkey="g i" data-analytics-event="{&quot;category&quot;:&quot;Global navigation&quot;,&quot;action&quot;:&quot;ISSUES&quot;,&quot;label&quot;:null}" id="item-c8d41e32-ee08-4935-b851-76561809da78" href="https://github.com/issues" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-issue-opened">
    <path d="M8 9.5a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3Z"></path><path d="M8 0a8 8 0 1 1 0 16A8 8 0 0 1 8 0ZM1.5 8a6.5 6.5 0 1 0 13 0 6.5 6.5 0 0 0-13 0Z"></path>
</svg>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
          Issues
</span>      
</a>
  
</li>

        
          
<li data-item-id="" data-targets="nav-list.items" data-view-component="true" class="ActionListItem">
    
    
    <a data-hotkey="g p" data-analytics-event="{&quot;category&quot;:&quot;Global navigation&quot;,&quot;action&quot;:&quot;PULL_REQUESTS&quot;,&quot;label&quot;:null}" id="item-7e7ae222-f866-43dc-9e6b-a37888a72c27" href="https://github.com/pulls" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-git-pull-request">
    <path d="M1.5 3.25a2.25 2.25 0 1 1 3 2.122v5.256a2.251 2.251 0 1 1-1.5 0V5.372A2.25 2.25 0 0 1 1.5 3.25Zm5.677-.177L9.573.677A.25.25 0 0 1 10 .854V2.5h1A2.5 2.5 0 0 1 13.5 5v5.628a2.251 2.251 0 1 1-1.5 0V5a1 1 0 0 0-1-1h-1v1.646a.25.25 0 0 1-.427.177L7.177 3.427a.25.25 0 0 1 0-.354ZM3.75 2.5a.75.75 0 1 0 0 1.5.75.75 0 0 0 0-1.5Zm0 9.5a.75.75 0 1 0 0 1.5.75.75 0 0 0 0-1.5Zm8.25.75a.75.75 0 1 0 1.5 0 .75.75 0 0 0-1.5 0Z"></path>
</svg>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
          Pull requests
</span>      
</a>
  
</li>

        
          
<li data-item-id="" data-targets="nav-list.items" data-view-component="true" class="ActionListItem">
    
    
    <a data-analytics-event="{&quot;category&quot;:&quot;Global navigation&quot;,&quot;action&quot;:&quot;PROJECTS&quot;,&quot;label&quot;:null}" id="item-b20501da-fd20-4bff-b65b-52f4dc84d254" href="https://github.com/projects" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-table">
    <path d="M0 1.75C0 .784.784 0 1.75 0h12.5C15.216 0 16 .784 16 1.75v12.5A1.75 1.75 0 0 1 14.25 16H1.75A1.75 1.75 0 0 1 0 14.25ZM6.5 6.5v8h7.75a.25.25 0 0 0 .25-.25V6.5Zm8-1.5V1.75a.25.25 0 0 0-.25-.25H6.5V5Zm-13 1.5v7.75c0 .138.112.25.25.25H5v-8ZM5 5V1.5H1.75a.25.25 0 0 0-.25.25V5Z"></path>
</svg>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
          Projects
</span>      
</a>
  
</li>

        
          
<li data-item-id="" data-targets="nav-list.items" data-view-component="true" class="ActionListItem">
    
    
    <a data-analytics-event="{&quot;category&quot;:&quot;Global navigation&quot;,&quot;action&quot;:&quot;DISCUSSIONS&quot;,&quot;label&quot;:null}" id="item-fb039c52-6904-478e-8248-d4d01a4e484e" href="https://github.com/discussions" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-comment-discussion">
    <path d="M1.75 1h8.5c.966 0 1.75.784 1.75 1.75v5.5A1.75 1.75 0 0 1 10.25 10H7.061l-2.574 2.573A1.458 1.458 0 0 1 2 11.543V10h-.25A1.75 1.75 0 0 1 0 8.25v-5.5C0 1.784.784 1 1.75 1ZM1.5 2.75v5.5c0 .138.112.25.25.25h1a.75.75 0 0 1 .75.75v2.19l2.72-2.72a.749.749 0 0 1 .53-.22h3.5a.25.25 0 0 0 .25-.25v-5.5a.25.25 0 0 0-.25-.25h-8.5a.25.25 0 0 0-.25.25Zm13 2a.25.25 0 0 0-.25-.25h-.5a.75.75 0 0 1 0-1.5h.5c.966 0 1.75.784 1.75 1.75v5.5A1.75 1.75 0 0 1 14.25 12H14v1.543a1.458 1.458 0 0 1-2.487 1.03L9.22 12.28a.749.749 0 0 1 .326-1.275.749.749 0 0 1 .734.215l2.22 2.22v-2.19a.75.75 0 0 1 .75-.75h1a.25.25 0 0 0 .25-.25Z"></path>
</svg>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
          Discussions
</span>      
</a>
  
</li>

        
          
<li data-item-id="" data-targets="nav-list.items" data-view-component="true" class="ActionListItem">
    
    
    <a data-analytics-event="{&quot;category&quot;:&quot;Global navigation&quot;,&quot;action&quot;:&quot;CODESPACES&quot;,&quot;label&quot;:null}" id="item-bcf4cf27-d954-4230-a611-c3f8ed7cb1c8" href="https://github.com/codespaces" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-codespaces">
    <path d="M0 11.25c0-.966.784-1.75 1.75-1.75h12.5c.966 0 1.75.784 1.75 1.75v3A1.75 1.75 0 0 1 14.25 16H1.75A1.75 1.75 0 0 1 0 14.25Zm2-9.5C2 .784 2.784 0 3.75 0h8.5C13.216 0 14 .784 14 1.75v5a1.75 1.75 0 0 1-1.75 1.75h-8.5A1.75 1.75 0 0 1 2 6.75Zm1.75-.25a.25.25 0 0 0-.25.25v5c0 .138.112.25.25.25h8.5a.25.25 0 0 0 .25-.25v-5a.25.25 0 0 0-.25-.25Zm-2 9.5a.25.25 0 0 0-.25.25v3c0 .138.112.25.25.25h12.5a.25.25 0 0 0 .25-.25v-3a.25.25 0 0 0-.25-.25Z"></path><path d="M7 12.75a.75.75 0 0 1 .75-.75h4.5a.75.75 0 0 1 0 1.5h-4.5a.75.75 0 0 1-.75-.75Zm-4 0a.75.75 0 0 1 .75-.75h.5a.75.75 0 0 1 0 1.5h-.5a.75.75 0 0 1-.75-.75Z"></path>
</svg>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
          Codespaces
</span>      
</a>
  
</li>

        
          
<li data-item-id="" data-targets="nav-list.items" data-view-component="true" class="ActionListItem">
    
    
    <a data-analytics-event="{&quot;category&quot;:&quot;Global navigation&quot;,&quot;action&quot;:&quot;COPILOT&quot;,&quot;label&quot;:null}" id="item-9802e9fb-4442-4c95-9169-debfb8c2e1dc" href="https://github.com/copilot" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-copilot">
    <path d="M7.998 15.035c-4.562 0-7.873-2.914-7.998-3.749V9.338c.085-.628.677-1.686 1.588-2.065.013-.07.024-.143.036-.218.029-.183.06-.384.126-.612-.201-.508-.254-1.084-.254-1.656 0-.87.128-1.769.693-2.484.579-.733 1.494-1.124 2.724-1.261 1.206-.134 2.262.034 2.944.765.05.053.096.108.139.165.044-.057.094-.112.143-.165.682-.731 1.738-.899 2.944-.765 1.23.137 2.145.528 2.724 1.261.566.715.693 1.614.693 2.484 0 .572-.053 1.148-.254 1.656.066.228.098.429.126.612.012.076.024.148.037.218.924.385 1.522 1.471 1.591 2.095v1.872c0 .766-3.351 3.795-8.002 3.795Zm0-1.485c2.28 0 4.584-1.11 5.002-1.433V7.862l-.023-.116c-.49.21-1.075.291-1.727.291-1.146 0-2.059-.327-2.71-.991A3.222 3.222 0 0 1 8 6.303a3.24 3.24 0 0 1-.544.743c-.65.664-1.563.991-2.71.991-.652 0-1.236-.081-1.727-.291l-.023.116v4.255c.419.323 2.722 1.433 5.002 1.433ZM6.762 2.83c-.193-.206-.637-.413-1.682-.297-1.019.113-1.479.404-1.713.7-.247.312-.369.789-.369 1.554 0 .793.129 1.171.308 1.371.162.181.519.379 1.442.379.853 0 1.339-.235 1.638-.54.315-.322.527-.827.617-1.553.117-.935-.037-1.395-.241-1.614Zm4.155-.297c-1.044-.116-1.488.091-1.681.297-.204.219-.359.679-.242 1.614.091.726.303 1.231.618 1.553.299.305.784.54 1.638.54.922 0 1.28-.198 1.442-.379.179-.2.308-.578.308-1.371 0-.765-.123-1.242-.37-1.554-.233-.296-.693-.587-1.713-.7Z"></path><path d="M6.25 9.037a.75.75 0 0 1 .75.75v1.501a.75.75 0 0 1-1.5 0V9.787a.75.75 0 0 1 .75-.75Zm4.25.75v1.501a.75.75 0 0 1-1.5 0V9.787a.75.75 0 0 1 1.5 0Z"></path>
</svg>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
          Copilot
</span>      
</a>
  
</li>

        
          <li role="presentation" aria-hidden="true" data-view-component="true" class="ActionList-sectionDivider"></li>
        
          
<li data-item-id="" data-targets="nav-list.items" data-view-component="true" class="ActionListItem">
    
    
    <a data-analytics-event="{&quot;category&quot;:&quot;Global navigation&quot;,&quot;action&quot;:&quot;EXPLORE&quot;,&quot;label&quot;:null}" id="item-6e5f48fc-5439-4384-b78b-1e379cf15223" href="https://github.com/explore" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-telescope">
    <path d="M14.184 1.143v-.001l1.422 2.464a1.75 1.75 0 0 1-.757 2.451L3.104 11.713a1.75 1.75 0 0 1-2.275-.702l-.447-.775a1.75 1.75 0 0 1 .53-2.32L11.682.573a1.748 1.748 0 0 1 2.502.57Zm-4.709 9.32h-.001l2.644 3.863a.75.75 0 1 1-1.238.848l-1.881-2.75v2.826a.75.75 0 0 1-1.5 0v-2.826l-1.881 2.75a.75.75 0 1 1-1.238-.848l2.049-2.992a.746.746 0 0 1 .293-.253l1.809-.87a.749.749 0 0 1 .944.252ZM9.436 3.92h-.001l-4.97 3.39.942 1.63 5.42-2.61Zm3.091-2.108h.001l-1.85 1.26 1.505 2.605 2.016-.97a.247.247 0 0 0 .13-.151.247.247 0 0 0-.022-.199l-1.422-2.464a.253.253 0 0 0-.161-.119.254.254 0 0 0-.197.038ZM1.756 9.157a.25.25 0 0 0-.075.33l.447.775a.25.25 0 0 0 .325.1l1.598-.769-.83-1.436-1.465 1Z"></path>
</svg>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
          Explore
</span>      
</a>
  
</li>

        
          
<li data-item-id="" data-targets="nav-list.items" data-view-component="true" class="ActionListItem">
    
    
    <a data-analytics-event="{&quot;category&quot;:&quot;Global navigation&quot;,&quot;action&quot;:&quot;MARKETPLACE&quot;,&quot;label&quot;:null}" id="item-b8591eef-8da9-4e9a-8b50-bb6f9777b80a" href="https://github.com/marketplace" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-gift">
    <path d="M2 2.75A2.75 2.75 0 0 1 4.75 0c.983 0 1.873.42 2.57 1.232.268.318.497.668.68 1.042.183-.375.411-.725.68-1.044C9.376.42 10.266 0 11.25 0a2.75 2.75 0 0 1 2.45 4h.55c.966 0 1.75.784 1.75 1.75v2c0 .698-.409 1.301-1 1.582v4.918A1.75 1.75 0 0 1 13.25 16H2.75A1.75 1.75 0 0 1 1 14.25V9.332C.409 9.05 0 8.448 0 7.75v-2C0 4.784.784 4 1.75 4h.55c-.192-.375-.3-.8-.3-1.25ZM7.25 9.5H2.5v4.75c0 .138.112.25.25.25h4.5Zm1.5 0v5h4.5a.25.25 0 0 0 .25-.25V9.5Zm0-4V8h5.5a.25.25 0 0 0 .25-.25v-2a.25.25 0 0 0-.25-.25Zm-7 0a.25.25 0 0 0-.25.25v2c0 .138.112.25.25.25h5.5V5.5h-5.5Zm3-4a1.25 1.25 0 0 0 0 2.5h2.309c-.233-.818-.542-1.401-.878-1.793-.43-.502-.915-.707-1.431-.707ZM8.941 4h2.309a1.25 1.25 0 0 0 0-2.5c-.516 0-1 .205-1.43.707-.337.392-.646.975-.879 1.793Z"></path>
</svg>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
          Marketplace
</span>      
</a>
  
</li>

</ul>  </nav-list>
</nav>

        <div data-view-component="true" class="my-3 d-flex flex-justify-center height-full">
          <span data-view-component="true">
  <svg style="box-sizing: content-box; color: var(--color-icon-primary);" width="16" height="16" viewBox="0 0 16 16" fill="none" aria-hidden="true" data-view-component="true" class="anim-rotate">
    <circle cx="8" cy="8" r="7" stroke="currentColor" stroke-opacity="0.25" stroke-width="2" vector-effect="non-scaling-stroke" fill="none"></circle>
    <path d="M15 8a7.002 7.002 0 00-7-7" stroke="currentColor" stroke-width="2" stroke-linecap="round" vector-effect="non-scaling-stroke"></path>
</svg>    <span class="sr-only">Loading</span>
</span>
</div>
</div>
      <div data-view-component="true" class="flex-1"></div>


      <div data-view-component="true" class="px-2">      <p class="color-fg-subtle text-small text-light">© 2025 GitHub, Inc.</p>

      <div data-view-component="true" class="d-flex flex-wrap text-small text-light">
          <a target="_blank" href="https://github.com/about" data-view-component="true" class="Link mr-2">About</a>
          <a target="_blank" href="https://github.blog/" data-view-component="true" class="Link mr-2">Blog</a>
          <a target="_blank" href="https://docs.github.com/site-policy/github-terms/github-terms-of-service" data-view-component="true" class="Link mr-2">Terms</a>
          <a target="_blank" href="https://docs.github.com/site-policy/privacy-policies/github-privacy-statement" data-view-component="true" class="Link mr-2">Privacy</a>
          <a target="_blank" href="https://github.com/security" data-view-component="true" class="Link mr-2">Security</a>
          <a target="_blank" href="https://www.githubstatus.com/" data-view-component="true" class="Link mr-3">Status</a>

</div></div>
</div>
      </scrollable-region>
      
</dialog></dialog-helper>


  <div data-show-on-forbidden-error="" hidden="">
    <div class="Box">
  <div class="blankslate-container">
    <div data-view-component="true" class="blankslate blankslate-spacious color-bg-default rounded-2">
      

      <h3 data-view-component="true" class="blankslate-heading">        Uh oh!
</h3>
      <p data-view-component="true">        </p><p class="color-fg-muted my-2 mb-2 ws-normal">There was an error while loading. <a class="Link--inTextBlock" data-turbo="false" href="https://github.com/fastabyq/-Deploy_ke_Streamlit_Cloud/blob/main/app.py" aria-label="Please reload this page">Please reload this page</a>.</p>
<p></p>

</div>  </div>
</div>  </div>
</include-fragment></deferred-side-panel>
        </div>

        <a class="AppHeader-logo ml-1 " href="https://github.com/" data-hotkey="g d" aria-label="Homepage " data-turbo="false" data-analytics-event="{&quot;category&quot;:&quot;Header&quot;,&quot;action&quot;:&quot;go to dashboard&quot;,&quot;label&quot;:&quot;icon:logo&quot;}">
          <svg height="32" aria-hidden="true" viewBox="0 0 24 24" version="1.1" width="32" data-view-component="true" class="octicon octicon-mark-github v-align-middle">
    <path d="M12 1C5.9225 1 1 5.9225 1 12C1 16.8675 4.14875 20.9787 8.52125 22.4362C9.07125 22.5325 9.2775 22.2025 9.2775 21.9137C9.2775 21.6525 9.26375 20.7862 9.26375 19.865C6.5 20.3737 5.785 19.1912 5.565 18.5725C5.44125 18.2562 4.905 17.28 4.4375 17.0187C4.0525 16.8125 3.5025 16.3037 4.42375 16.29C5.29 16.2762 5.90875 17.0875 6.115 17.4175C7.105 19.0812 8.68625 18.6137 9.31875 18.325C9.415 17.61 9.70375 17.1287 10.02 16.8537C7.5725 16.5787 5.015 15.63 5.015 11.4225C5.015 10.2262 5.44125 9.23625 6.1425 8.46625C6.0325 8.19125 5.6475 7.06375 6.2525 5.55125C6.2525 5.55125 7.17375 5.2625 9.2775 6.67875C10.1575 6.43125 11.0925 6.3075 12.0275 6.3075C12.9625 6.3075 13.8975 6.43125 14.7775 6.67875C16.8813 5.24875 17.8025 5.55125 17.8025 5.55125C18.4075 7.06375 18.0225 8.19125 17.9125 8.46625C18.6138 9.23625 19.04 10.2125 19.04 11.4225C19.04 15.6437 16.4688 16.5787 14.0213 16.8537C14.42 17.1975 14.7638 17.8575 14.7638 18.8887C14.7638 20.36 14.75 21.5425 14.75 21.9137C14.75 22.2025 14.9563 22.5462 15.5063 22.4362C19.8513 20.9787 23 16.8537 23 12C23 5.9225 18.0775 1 12 1Z"></path>
</svg>
        </a>

          <context-region-controller class="AppHeader-context responsive-context-region" data-is-responsive="" data-max-items="5" data-catalyst="">

  <div class="AppHeader-context-full">
    <nav role="navigation" aria-label="GitHub Breadcrumb">
        
<context-region data-target="context-region-controller.contextRegion" role="list" data-action="context-region-changed:context-region-controller#crumbsChanged" data-is-responsive="" data-catalyst="">
    <context-region-crumb data-crumb-id="contextregion-usercrumb-fastabyq" data-targets="context-region.crumbs" data-label="fastabyq" data-href="/fastabyq" data-pre-rendered="" data-is-responsive="" role="listitem" data-catalyst="">
      <a data-analytics-event="{&quot;category&quot;:&quot;SiteHeaderComponent&quot;,&quot;action&quot;:&quot;context_region_crumb&quot;,&quot;label&quot;:&quot;fastabyq&quot;,&quot;screen_size&quot;:&quot;full&quot;}" data-hovercard-type="user" data-hovercard-url="/users/fastabyq/hovercard" data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" data-target="context-region-crumb.linkElement" href="https://github.com/fastabyq" id="contextregion-usercrumb-fastabyq-link" data-view-component="true" class="AppHeader-context-item">
        <span data-target="context-region-crumb.labelElement" class="AppHeader-context-item-label ">fastabyq</span>

</a><tool-tip data-target="context-region-crumb.tooltip" for="contextregion-usercrumb-fastabyq-link" popover="manual" class="sr-only" position="absolute" data-type="label" data-direction="s" hidden="" role="tooltip"><template shadowrootmode="open"><style>
      :host {
        --tooltip-top: var(--tool-tip-position-top, 0);
        --tooltip-left: var(--tool-tip-position-left, 0);
        padding: var(--overlay-paddingBlock-condensed) var(--overlay-padding-condensed) !important;
        font: var(--text-body-shorthand-small);
        color: var(--tooltip-fgColor, var(--fgColor-onEmphasis)) !important;
        text-align: center;
        text-decoration: none;
        text-shadow: none;
        text-transform: none;
        letter-spacing: normal;
        word-wrap: break-word;
        white-space: pre;
        background: var(--tooltip-bgColor, var(--bgColor-emphasis)) !important;
        border-radius: var(--borderRadius-medium);
        border: 0 !important;
        opacity: 0;
        max-width: var(--overlay-width-small);
        word-wrap: break-word;
        white-space: normal;
        width: max-content !important;
        inset: var(--tooltip-top) auto auto var(--tooltip-left) !important;
        overflow: visible !important;
        text-wrap: balance;
      }

      :host(:is(.tooltip-n, .tooltip-nw, .tooltip-ne)) {
        --tooltip-top: calc(var(--tool-tip-position-top, 0) - var(--overlay-offset, 0.25rem));
        --tooltip-left: var(--tool-tip-position-left);
      }

      :host(:is(.tooltip-s, .tooltip-sw, .tooltip-se)) {
        --tooltip-top: calc(var(--tool-tip-position-top, 0) + var(--overlay-offset, 0.25rem));
        --tooltip-left: var(--tool-tip-position-left);
      }

      :host(.tooltip-w) {
        --tooltip-top: var(--tool-tip-position-top);
        --tooltip-left: calc(var(--tool-tip-position-left, 0) - var(--overlay-offset, 0.25rem));
      }

      :host(.tooltip-e) {
        --tooltip-top: var(--tool-tip-position-top);
        --tooltip-left: calc(var(--tool-tip-position-left, 0) + var(--overlay-offset, 0.25rem));
      }

      :host:after{
        position: absolute;
        display: block;
        right: 0;
        left: 0;
        height: var(--overlay-offset, 0.25rem);
        content: "";
      }

      :host(.tooltip-s):after,
      :host(.tooltip-se):after,
      :host(.tooltip-sw):after {
        bottom: 100%
      }

      :host(.tooltip-n):after,
      :host(.tooltip-ne):after,
      :host(.tooltip-nw):after {
        top: 100%;
      }

      @keyframes tooltip-appear {
        from {
          opacity: 0;
        }
        to {
          opacity: 1;
        }
      }

      :host(:popover-open),
      :host(:popover-open):before {
        animation-name: tooltip-appear;
        animation-duration: .1s;
        animation-fill-mode: forwards;
        animation-timing-function: ease-in;
      }

      :host(.\:popover-open) {
        animation-name: tooltip-appear;
        animation-duration: .1s;
        animation-fill-mode: forwards;
        animation-timing-function: ease-in;
      }

      @media (forced-colors: active) {
        :host {
          outline: solid 1px transparent;
        }

        :host:before {
          display: none;
        }
      }
    </style><slot></slot></template>
          fastabyq
        </tool-tip>
      <context-region-divider data-target="context-region-crumb.dividerElement" data-pre-rendered="" data-catalyst="">
  <span class="AppHeader-context-item-separator">
    <span class="sr-only">/</span>
    <svg width="16" height="16" viewBox="0 0 16 16" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
      <path d="M10.956 1.27994L6.06418 14.7201L5 14.7201L9.89181 1.27994L10.956 1.27994Z" fill="currentcolor"></path>
    </svg>
  </span>
</context-region-divider>

    
        
      </context-region-crumb>

      <li data-target="context-region-controller.overflowMenuContainer context-region.overflowMenuContainer" role="listitem" hidden="">
        <action-menu data-target="context-region-controller.overflowActionMenu" data-select-variant="none" data-view-component="true" data-catalyst="" data-ready="true">
  <focus-group direction="vertical" mnemonics="" retain="">
    <button id="action-menu-dca0c240-ade5-4847-9223-962b7b132d3c-button" popovertarget="action-menu-dca0c240-ade5-4847-9223-962b7b132d3c-overlay" aria-controls="action-menu-dca0c240-ade5-4847-9223-962b7b132d3c-list" aria-haspopup="true" aria-labelledby="tooltip-9ec39476-d510-437e-809a-105a574e95da" type="button" data-view-component="true" class="Button Button--iconOnly Button--secondary Button--medium">  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-kebab-horizontal Button-visual">
    <path d="M8 9a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3ZM1.5 9a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3Zm13 0a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3Z"></path>
</svg>
</button><tool-tip id="tooltip-9ec39476-d510-437e-809a-105a574e95da" for="action-menu-dca0c240-ade5-4847-9223-962b7b132d3c-button" popover="manual" data-direction="s" data-type="label" data-view-component="true" class="sr-only position-absolute" aria-hidden="true" role="tooltip"><template shadowrootmode="open"><style>
      :host {
        --tooltip-top: var(--tool-tip-position-top, 0);
        --tooltip-left: var(--tool-tip-position-left, 0);
        padding: var(--overlay-paddingBlock-condensed) var(--overlay-padding-condensed) !important;
        font: var(--text-body-shorthand-small);
        color: var(--tooltip-fgColor, var(--fgColor-onEmphasis)) !important;
        text-align: center;
        text-decoration: none;
        text-shadow: none;
        text-transform: none;
        letter-spacing: normal;
        word-wrap: break-word;
        white-space: pre;
        background: var(--tooltip-bgColor, var(--bgColor-emphasis)) !important;
        border-radius: var(--borderRadius-medium);
        border: 0 !important;
        opacity: 0;
        max-width: var(--overlay-width-small);
        word-wrap: break-word;
        white-space: normal;
        width: max-content !important;
        inset: var(--tooltip-top) auto auto var(--tooltip-left) !important;
        overflow: visible !important;
        text-wrap: balance;
      }

      :host(:is(.tooltip-n, .tooltip-nw, .tooltip-ne)) {
        --tooltip-top: calc(var(--tool-tip-position-top, 0) - var(--overlay-offset, 0.25rem));
        --tooltip-left: var(--tool-tip-position-left);
      }

      :host(:is(.tooltip-s, .tooltip-sw, .tooltip-se)) {
        --tooltip-top: calc(var(--tool-tip-position-top, 0) + var(--overlay-offset, 0.25rem));
        --tooltip-left: var(--tool-tip-position-left);
      }

      :host(.tooltip-w) {
        --tooltip-top: var(--tool-tip-position-top);
        --tooltip-left: calc(var(--tool-tip-position-left, 0) - var(--overlay-offset, 0.25rem));
      }

      :host(.tooltip-e) {
        --tooltip-top: var(--tool-tip-position-top);
        --tooltip-left: calc(var(--tool-tip-position-left, 0) + var(--overlay-offset, 0.25rem));
      }

      :host:after{
        position: absolute;
        display: block;
        right: 0;
        left: 0;
        height: var(--overlay-offset, 0.25rem);
        content: "";
      }

      :host(.tooltip-s):after,
      :host(.tooltip-se):after,
      :host(.tooltip-sw):after {
        bottom: 100%
      }

      :host(.tooltip-n):after,
      :host(.tooltip-ne):after,
      :host(.tooltip-nw):after {
        top: 100%;
      }

      @keyframes tooltip-appear {
        from {
          opacity: 0;
        }
        to {
          opacity: 1;
        }
      }

      :host(:popover-open),
      :host(:popover-open):before {
        animation-name: tooltip-appear;
        animation-duration: .1s;
        animation-fill-mode: forwards;
        animation-timing-function: ease-in;
      }

      :host(.\:popover-open) {
        animation-name: tooltip-appear;
        animation-duration: .1s;
        animation-fill-mode: forwards;
        animation-timing-function: ease-in;
      }

      @media (forced-colors: active) {
        :host {
          outline: solid 1px transparent;
        }

        :host:before {
          display: none;
        }
      }
    </style><slot></slot></template>Show more breadcrumb items</tool-tip>


<anchored-position data-target="action-menu.overlay" id="action-menu-dca0c240-ade5-4847-9223-962b7b132d3c-overlay" anchor="action-menu-dca0c240-ade5-4847-9223-962b7b132d3c-button" align="start" side="outside-bottom" anchor-offset="normal" popover="auto" data-view-component="true" style="inset: 4px auto auto 0px;">
  <div data-view-component="true" class="Overlay Overlay--size-auto">
    
      <div data-view-component="true" class="Overlay-body Overlay-body--paddingNone">          <action-list data-catalyst="">
  <div data-view-component="true">
    <ul aria-labelledby="action-menu-dca0c240-ade5-4847-9223-962b7b132d3c-button" id="action-menu-dca0c240-ade5-4847-9223-962b7b132d3c-list" role="menu" data-view-component="true" class="ActionListWrap--inset ActionListWrap">
        <li hidden="true" data-crumb-id="contextregion-usercrumb-fastabyq" data-targets="context-region.overflowCrumbs action-list.items" data-analytics-event="{&quot;category&quot;:&quot;SiteHeaderComponent&quot;,&quot;action&quot;:&quot;context_region_overflow_menu_crumb&quot;,&quot;label&quot;:&quot;global-navigation&quot;}" role="none" data-view-component="true" class="ActionListItem">
    
    
    <a tabindex="-1" id="item-1a797280-75cb-4226-97aa-bf13ffa9635a" href="https://github.com/fastabyq" role="menuitem" data-view-component="true" class="ActionListContent">
      
        <span data-view-component="true" class="ActionListItem-label">
          fastabyq
</span>      
</a>
  
</li>
        <li hidden="true" data-crumb-id="contextregion-repositorycrumb-deploy_ke_streamlit_cloud" data-targets="context-region.overflowCrumbs action-list.items" data-analytics-event="{&quot;category&quot;:&quot;SiteHeaderComponent&quot;,&quot;action&quot;:&quot;context_region_overflow_menu_crumb&quot;,&quot;label&quot;:&quot;global-navigation&quot;}" role="none" data-view-component="true" class="ActionListItem">
    
    
    <a tabindex="-1" id="item-571db801-aab9-45f9-a2be-3d5324595174" href="https://github.com/fastabyq/-Deploy_ke_Streamlit_Cloud" role="menuitem" data-view-component="true" class="ActionListContent">
      
        <span data-view-component="true" class="ActionListItem-label">
          -Deploy_ke_Streamlit_Cloud
</span>      
</a>
  
</li>
</ul>    
</div></action-list>


</div>
      
</div></anchored-position>  </focus-group>
</action-menu>
  <context-region-divider data-target="context-region-crumb.dividerElement" data-pre-rendered="" data-catalyst="">
  <span class="AppHeader-context-item-separator">
    <span class="sr-only">/</span>
    <svg width="16" height="16" viewBox="0 0 16 16" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
      <path d="M10.956 1.27994L6.06418 14.7201L5 14.7201L9.89181 1.27994L10.956 1.27994Z" fill="currentcolor"></path>
    </svg>
  </span>
</context-region-divider>


      </li>
    <context-region-crumb data-crumb-id="contextregion-repositorycrumb-deploy_ke_streamlit_cloud" data-targets="context-region.crumbs" data-label="-Deploy_ke_Streamlit_Cloud" data-href="/fastabyq/-Deploy_ke_Streamlit_Cloud" data-pre-rendered="" data-is-responsive="" role="listitem" data-catalyst="">
      <a data-analytics-event="{&quot;category&quot;:&quot;SiteHeaderComponent&quot;,&quot;action&quot;:&quot;context_region_crumb&quot;,&quot;label&quot;:&quot;-Deploy_ke_Streamlit_Cloud&quot;,&quot;screen_size&quot;:&quot;full&quot;}" data-target="context-region-crumb.linkElement" href="https://github.com/fastabyq/-Deploy_ke_Streamlit_Cloud" id="contextregion-repositorycrumb-deploy_ke_streamlit_cloud-link" data-view-component="true" class="AppHeader-context-item">
        <span data-target="context-region-crumb.labelElement" class="AppHeader-context-item-label ">-Deploy_ke_Streamlit_Cloud</span>

</a><tool-tip data-target="context-region-crumb.tooltip" for="contextregion-repositorycrumb-deploy_ke_streamlit_cloud-link" popover="manual" class="sr-only" position="absolute" data-type="label" data-direction="s" hidden="true" role="tooltip"><template shadowrootmode="open"><style>
      :host {
        --tooltip-top: var(--tool-tip-position-top, 0);
        --tooltip-left: var(--tool-tip-position-left, 0);
        padding: var(--overlay-paddingBlock-condensed) var(--overlay-padding-condensed) !important;
        font: var(--text-body-shorthand-small);
        color: var(--tooltip-fgColor, var(--fgColor-onEmphasis)) !important;
        text-align: center;
        text-decoration: none;
        text-shadow: none;
        text-transform: none;
        letter-spacing: normal;
        word-wrap: break-word;
        white-space: pre;
        background: var(--tooltip-bgColor, var(--bgColor-emphasis)) !important;
        border-radius: var(--borderRadius-medium);
        border: 0 !important;
        opacity: 0;
        max-width: var(--overlay-width-small);
        word-wrap: break-word;
        white-space: normal;
        width: max-content !important;
        inset: var(--tooltip-top) auto auto var(--tooltip-left) !important;
        overflow: visible !important;
        text-wrap: balance;
      }

      :host(:is(.tooltip-n, .tooltip-nw, .tooltip-ne)) {
        --tooltip-top: calc(var(--tool-tip-position-top, 0) - var(--overlay-offset, 0.25rem));
        --tooltip-left: var(--tool-tip-position-left);
      }

      :host(:is(.tooltip-s, .tooltip-sw, .tooltip-se)) {
        --tooltip-top: calc(var(--tool-tip-position-top, 0) + var(--overlay-offset, 0.25rem));
        --tooltip-left: var(--tool-tip-position-left);
      }

      :host(.tooltip-w) {
        --tooltip-top: var(--tool-tip-position-top);
        --tooltip-left: calc(var(--tool-tip-position-left, 0) - var(--overlay-offset, 0.25rem));
      }

      :host(.tooltip-e) {
        --tooltip-top: var(--tool-tip-position-top);
        --tooltip-left: calc(var(--tool-tip-position-left, 0) + var(--overlay-offset, 0.25rem));
      }

      :host:after{
        position: absolute;
        display: block;
        right: 0;
        left: 0;
        height: var(--overlay-offset, 0.25rem);
        content: "";
      }

      :host(.tooltip-s):after,
      :host(.tooltip-se):after,
      :host(.tooltip-sw):after {
        bottom: 100%
      }

      :host(.tooltip-n):after,
      :host(.tooltip-ne):after,
      :host(.tooltip-nw):after {
        top: 100%;
      }

      @keyframes tooltip-appear {
        from {
          opacity: 0;
        }
        to {
          opacity: 1;
        }
      }

      :host(:popover-open),
      :host(:popover-open):before {
        animation-name: tooltip-appear;
        animation-duration: .1s;
        animation-fill-mode: forwards;
        animation-timing-function: ease-in;
      }

      :host(.\:popover-open) {
        animation-name: tooltip-appear;
        animation-duration: .1s;
        animation-fill-mode: forwards;
        animation-timing-function: ease-in;
      }

      @media (forced-colors: active) {
        :host {
          outline: solid 1px transparent;
        }

        :host:before {
          display: none;
        }
      }
    </style><slot></slot></template>
          -Deploy_ke_Streamlit_Cloud
        </tool-tip>
      <context-region-divider data-target="context-region-crumb.dividerElement" data-pre-rendered="" data-catalyst="">
  <span class="AppHeader-context-item-separator">
    <span class="sr-only">/</span>
    <svg width="16" height="16" viewBox="0 0 16 16" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
      <path d="M10.956 1.27994L6.06418 14.7201L5 14.7201L9.89181 1.27994L10.956 1.27994Z" fill="currentcolor"></path>
    </svg>
  </span>
</context-region-divider>

    
        
      </context-region-crumb>

</context-region>

    </nav>
  </div>
</context-region-controller>

      </div>
      <div class="AppHeader-globalBar-end">
          <div class="AppHeader-search">
              


<qbsearch-input class="search-input" data-scope="repo:fastabyq/-Deploy_ke_Streamlit_Cloud" data-custom-scopes-path="/search/custom_scopes" data-delete-custom-scopes-csrf="5bcyZLRuqdAWvmadDrSd7T8FlQip6H474h8t5UkV63bJ3rszIk6ewpHjvplEK0lQocFheTpZBRmLebBU6JPpgA" data-max-custom-scopes="10" data-header-redesign-enabled="true" data-initial-value="" data-blackbird-suggestions-path="/search/suggestions" data-jump-to-suggestions-path="/_graphql/GetSuggestedNavigationDestinations" data-current-repository="fastabyq/-Deploy_ke_Streamlit_Cloud" data-current-org="" data-current-owner="fastabyq" data-logged-in="true" data-copilot-chat-enabled="true" data-nl-search-enabled="false" data-catalyst="">
  <div class="search-input-container search-with-dialog position-relative d-flex flex-row flex-items-center height-auto color-bg-transparent border-0 color-fg-subtle mx-0" data-action="click:qbsearch-input#searchInputContainerClicked">
      
            <button type="button" data-action="click:qbsearch-input#handleExpand" class="AppHeader-button AppHeader-search-whenNarrow" aria-label="Search or jump to…" aria-expanded="false" aria-haspopup="dialog">
            <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-search">
    <path d="M10.68 11.74a6 6 0 0 1-7.922-8.982 6 6 0 0 1 8.982 7.922l3.04 3.04a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215ZM11.5 7a4.499 4.499 0 1 0-8.997 0A4.499 4.499 0 0 0 11.5 7Z"></path>
</svg>
          </button>


<div class="AppHeader-search-whenRegular">
  <div class="AppHeader-search-wrap AppHeader-search-wrap--hasTrailing">
    <div class="AppHeader-search-control AppHeader-search-control-overflow">
      <label for="AppHeader-searchInput" aria-label="Search or jump to…" class="AppHeader-search-visual--leading">
        <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-search">
    <path d="M10.68 11.74a6 6 0 0 1-7.922-8.982 6 6 0 0 1 8.982 7.922l3.04 3.04a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215ZM11.5 7a4.499 4.499 0 1 0-8.997 0A4.499 4.499 0 0 0 11.5 7Z"></path>
</svg>
      </label>

                <button type="button" data-target="qbsearch-input.inputButton" data-action="click:qbsearch-input#handleExpand" class="AppHeader-searchButton form-control input-contrast text-left color-fg-subtle no-wrap placeholder" data-hotkey="s,/" data-analytics-event="{&quot;location&quot;:&quot;navbar&quot;,&quot;action&quot;:&quot;searchbar&quot;,&quot;context&quot;:&quot;global&quot;,&quot;tag&quot;:&quot;input&quot;,&quot;label&quot;:&quot;searchbar_input_global_navbar&quot;}" aria-describedby="search-error-message-flash">
            <div class="overflow-hidden">
              <span id="qb-input-query" data-target="qbsearch-input.inputButtonText">
                  Type <kbd class="AppHeader-search-kbd">/</kbd> to search
              </span>
            </div>
          </button>

    </div>


  </div>
</div>

    <input type="hidden" name="type" class="js-site-search-type-field">

    
<div class="Overlay--hidden " data-modal-dialog-overlay="">
  <modal-dialog data-action="close:qbsearch-input#handleClose cancel:qbsearch-input#handleClose" data-target="qbsearch-input.searchSuggestionsDialog" role="dialog" id="search-suggestions-dialog" aria-modal="true" aria-labelledby="search-suggestions-dialog-header" data-view-component="true" class="Overlay Overlay--width-medium Overlay--height-auto">
      <h1 id="search-suggestions-dialog-header" class="sr-only">Search code, repositories, users, issues, pull requests...</h1>
    <div class="Overlay-body Overlay-body--paddingNone">
      
          <div data-view-component="true">        <div class="search-suggestions position-absolute width-full color-shadow-large border color-fg-default color-bg-default overflow-hidden d-flex flex-column query-builder-container" style="border-radius: 12px;" data-target="qbsearch-input.queryBuilderContainer" hidden="">
          <!-- '"` --><!-- </textarea></xmp> --><form id="query-builder-test-form" action="https://github.com/fastabyq/-Deploy_ke_Streamlit_Cloud/blob/main/app.py" accept-charset="UTF-8" method="get">
  <query-builder data-target="qbsearch-input.queryBuilder" id="query-builder-query-builder-test" data-filter-key=":" data-view-component="true" class="QueryBuilder search-query-builder" data-min-width="300" data-catalyst="">
    <div class="FormControl FormControl--fullWidth">
      <label id="query-builder-test-label" for="query-builder-test" class="FormControl-label sr-only">
        Search
      </label>
      <div class="QueryBuilder-StyledInput width-fit " data-target="query-builder.styledInput">
          <span id="query-builder-test-leadingvisual-wrap" class="FormControl-input-leadingVisualWrap QueryBuilder-leadingVisualWrap">
            <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-search FormControl-input-leadingVisual">
    <path d="M10.68 11.74a6 6 0 0 1-7.922-8.982 6 6 0 0 1 8.982 7.922l3.04 3.04a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215ZM11.5 7a4.499 4.499 0 1 0-8.997 0A4.499 4.499 0 0 0 11.5 7Z"></path>
</svg>
          </span>
        <div data-target="query-builder.styledInputContainer" class="QueryBuilder-StyledInputContainer">
          <div aria-hidden="true" class="QueryBuilder-StyledInputContent" data-target="query-builder.styledInputContent"></div>
          <div class="QueryBuilder-InputWrapper">
            <div aria-hidden="true" class="QueryBuilder-Sizer" data-target="query-builder.sizer"><span></span></div>
            <input id="query-builder-test" name="query-builder-test" value="" autocomplete="off" type="text" role="combobox" spellcheck="false" aria-expanded="false" aria-describedby="validation-6f51303d-2ee9-4097-acb3-e4265700cae8" data-target="query-builder.input" data-action="
          input:query-builder#inputChange
          blur:query-builder#inputBlur
          keydown:query-builder#inputKeydown
          focus:query-builder#inputFocus
        " data-view-component="true" class="FormControl-input QueryBuilder-Input FormControl-medium" aria-controls="query-builder-test-results" aria-autocomplete="list" aria-haspopup="listbox" style="width: 300px;">
          </div>
        </div>
          <span class="sr-only" id="query-builder-test-clear">Clear</span>
          <button role="button" id="query-builder-test-clear-button" aria-labelledby="query-builder-test-clear query-builder-test-label" data-target="query-builder.clearButton" data-action="
                click:query-builder#clear
                focus:query-builder#clearButtonFocus
                blur:query-builder#clearButtonBlur
              " variant="small" hidden="" type="button" data-view-component="true" class="Button Button--iconOnly Button--invisible Button--medium mr-1 px-2 py-0 d-flex flex-items-center rounded-1 color-fg-muted">  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-x-circle-fill Button-visual">
    <path d="M2.343 13.657A8 8 0 1 1 13.658 2.343 8 8 0 0 1 2.343 13.657ZM6.03 4.97a.751.751 0 0 0-1.042.018.751.751 0 0 0-.018 1.042L6.94 8 4.97 9.97a.749.749 0 0 0 .326 1.275.749.749 0 0 0 .734-.215L8 9.06l1.97 1.97a.749.749 0 0 0 1.275-.326.749.749 0 0 0-.215-.734L9.06 8l1.97-1.97a.749.749 0 0 0-.326-1.275.749.749 0 0 0-.734.215L8 6.94Z"></path>
</svg>
</button>

      </div>
      <template id="search-icon"></template>

<template id="code-icon"></template>

<template id="file-code-icon"></template>

<template id="history-icon"></template>

<template id="repo-icon"></template>

<template id="bookmark-icon"></template>

<template id="plus-circle-icon"></template>

<template id="circle-icon"></template>

<template id="trash-icon"></template>

<template id="team-icon"></template>

<template id="project-icon"></template>

<template id="pencil-icon"></template>

<template id="copilot-icon"></template>

<template id="copilot-error-icon"></template>

<template id="workflow-icon"></template>

<template id="book-icon"></template>

<template id="code-review-icon"></template>

<template id="codespaces-icon"></template>

<template id="comment-icon"></template>

<template id="comment-discussion-icon"></template>

<template id="organization-icon"></template>

<template id="rocket-icon"></template>

<template id="shield-check-icon"></template>

<template id="heart-icon"></template>

<template id="server-icon"></template>

<template id="globe-icon"></template>

<template id="issue-opened-icon"></template>

<template id="device-mobile-icon"></template>

<template id="package-icon"></template>

<template id="credit-card-icon"></template>

<template id="play-icon"></template>

<template id="gift-icon"></template>

<template id="code-square-icon"></template>

<template id="device-desktop-icon"></template>

        <div class="position-relative">
                <ul role="listbox" class="ActionListWrap QueryBuilder-ListWrap" aria-label="Suggestions" data-action="
                    combobox-commit:query-builder#comboboxCommit
                    mousedown:query-builder#resultsMousedown
                  " data-target="query-builder.resultsList" data-persist-list="false" id="query-builder-test-results"></ul>
        </div>
      <div class="FormControl-inlineValidation" id="validation-6f51303d-2ee9-4097-acb3-e4265700cae8" hidden="hidden">
        <span class="FormControl-inlineValidation--visual">
          <svg aria-hidden="true" height="12" viewBox="0 0 12 12" version="1.1" width="12" data-view-component="true" class="octicon octicon-alert-fill">
    <path d="M4.855.708c.5-.896 1.79-.896 2.29 0l4.675 8.351a1.312 1.312 0 0 1-1.146 1.954H1.33A1.313 1.313 0 0 1 .183 9.058ZM7 7V3H5v4Zm-1 3a1 1 0 1 0 0-2 1 1 0 0 0 0 2Z"></path>
</svg>
        </span>
        <span></span>
</div>    </div>
    <div data-target="query-builder.screenReaderFeedback" aria-live="polite" aria-atomic="true" class="sr-only">0 suggestions.</div>
</query-builder></form>
          <div class="d-flex flex-row color-fg-muted px-3 text-small color-bg-default search-feedback-prompt">
            <a target="_blank" href="https://docs.github.com/search-github/github-code-search/understanding-github-code-search-syntax" data-view-component="true" class="Link color-fg-accent text-normal ml-2">Search syntax tips</a>            <div class="d-flex flex-1"></div>
              <button data-action="click:qbsearch-input#showFeedbackDialog" type="button" data-view-component="true" class="Button--link Button--medium Button color-fg-accent text-normal ml-2">  <span class="Button-content">
    <span class="Button-label">Give feedback</span>
  </span>
</button>
          </div>
        </div>
</div>

    </div>
</modal-dialog></div>
  </div>
  <div data-action="click:qbsearch-input#retract" class="dark-backdrop position-fixed" hidden="" data-target="qbsearch-input.darkBackdrop"></div>
  <div class="color-fg-default">
    
<dialog-helper>
  <dialog data-target="qbsearch-input.feedbackDialog" data-action="close:qbsearch-input#handleDialogClose cancel:qbsearch-input#handleDialogClose" id="feedback-dialog" aria-modal="true" aria-labelledby="feedback-dialog-title" aria-describedby="feedback-dialog-description" data-view-component="true" class="Overlay Overlay-whenNarrow Overlay--size-medium Overlay--motion-scaleFade Overlay--disableScroll">
    <div data-view-component="true" class="Overlay-header">
  <div class="Overlay-headerContentWrap">
    <div class="Overlay-titleWrap">
      <h1 class="Overlay-title " id="feedback-dialog-title">
        Provide feedback
      </h1>
        
    </div>
    <div class="Overlay-actionWrap">
      <button data-close-dialog-id="feedback-dialog" aria-label="Close" type="button" data-view-component="true" class="close-button Overlay-closeButton"><svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-x">
    <path d="M3.72 3.72a.75.75 0 0 1 1.06 0L8 6.94l3.22-3.22a.749.749 0 0 1 1.275.326.749.749 0 0 1-.215.734L9.06 8l3.22 3.22a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215L8 9.06l-3.22 3.22a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042L6.94 8 3.72 4.78a.75.75 0 0 1 0-1.06Z"></path>
</svg></button>
    </div>
  </div>
  
</div>
      <scrollable-region data-labelled-by="feedback-dialog-title" data-catalyst="" style="overflow: auto;">
        <div data-view-component="true" class="Overlay-body">        <!-- '"` --><!-- </textarea></xmp> --><form id="code-search-feedback-form" data-turbo="false" action="https://github.com/search/feedback" accept-charset="UTF-8" method="post"><input type="hidden" name="authenticity_token" value="L0t6kbHBsiK55Z1Mqm_TaEjDRtXFmJjsQdPiUViPcDp12wNbKUatqmnhhfQAkrCGNDDRbG-n7yxPgfMsSPjM8A">
          <p>We read every piece of feedback, and take your input very seriously.</p>
          <textarea name="feedback" class="form-control width-full mb-2" style="height: 120px" id="feedback"></textarea>
          <input name="include_email" id="include_email" aria-label="Include my email address so I can be contacted" class="form-control mr-2" type="checkbox">
          <label for="include_email" style="font-weight: normal">Include my email address so I can be contacted</label>
</form></div>
      </scrollable-region>
      <div data-view-component="true" class="Overlay-footer Overlay-footer--alignEnd">          <button data-close-dialog-id="feedback-dialog" type="button" data-view-component="true" class="btn">    Cancel
</button>
          <button form="code-search-feedback-form" data-action="click:qbsearch-input#submitFeedback" type="submit" data-view-component="true" class="btn-primary btn">    Submit feedback
</button>
</div>
</dialog></dialog-helper>

    <custom-scopes data-target="qbsearch-input.customScopesManager" data-catalyst="">
    
<dialog-helper>
  <dialog data-target="custom-scopes.customScopesModalDialog" data-action="close:qbsearch-input#handleDialogClose cancel:qbsearch-input#handleDialogClose" id="custom-scopes-dialog" aria-modal="true" aria-labelledby="custom-scopes-dialog-title" aria-describedby="custom-scopes-dialog-description" data-view-component="true" class="Overlay Overlay-whenNarrow Overlay--size-medium Overlay--motion-scaleFade Overlay--disableScroll">
    <div data-view-component="true" class="Overlay-header Overlay-header--divided">
  <div class="Overlay-headerContentWrap">
    <div class="Overlay-titleWrap">
      <h1 class="Overlay-title " id="custom-scopes-dialog-title">
        Saved searches
      </h1>
        <h2 id="custom-scopes-dialog-description" class="Overlay-description">Use saved searches to filter your results more quickly</h2>
    </div>
    <div class="Overlay-actionWrap">
      <button data-close-dialog-id="custom-scopes-dialog" aria-label="Close" type="button" data-view-component="true" class="close-button Overlay-closeButton"><svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-x">
    <path d="M3.72 3.72a.75.75 0 0 1 1.06 0L8 6.94l3.22-3.22a.749.749 0 0 1 1.275.326.749.749 0 0 1-.215.734L9.06 8l3.22 3.22a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215L8 9.06l-3.22 3.22a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042L6.94 8 3.72 4.78a.75.75 0 0 1 0-1.06Z"></path>
</svg></button>
    </div>
  </div>
  
</div>
      <scrollable-region data-labelled-by="custom-scopes-dialog-title" data-catalyst="" style="overflow: auto;">
        <div data-view-component="true" class="Overlay-body">        <div data-target="custom-scopes.customScopesModalDialogFlash"></div>

        <div hidden="" class="create-custom-scope-form" data-target="custom-scopes.createCustomScopeForm">
        <!-- '"` --><!-- </textarea></xmp> --><form id="custom-scopes-dialog-form" data-turbo="false" action="https://github.com/search/custom_scopes" accept-charset="UTF-8" method="post"><input type="hidden" name="authenticity_token" value="qvhq-2avYSBfhAo-pWA5Rl7KfuSJVOig2EZ9bvZNX-X1vxskmLrddxTy-1QbhFoy2gZxAA8GWSUyttdgdnMYfA">
          <div data-target="custom-scopes.customScopesModalDialogFlash"></div>

          <input type="hidden" id="custom_scope_id" name="custom_scope_id" data-target="custom-scopes.customScopesIdField">

          <div class="form-group">
            <label for="custom_scope_name">Name</label>
            <auto-check src="/search/custom_scopes/check_name" required="">
              <input type="text" name="custom_scope_name" id="custom_scope_name" data-target="custom-scopes.customScopesNameField" class="form-control" autocomplete="off" placeholder="github-ruby" required="" maxlength="50" spellcheck="false">
              <input type="hidden" value="hf4xb5wFBbarPiZ3bnVwPVCCWloam1jaIiZdFloFVxMC1d7uJ2stkUcjno9Pw6MUZP-vyTUd-nR4fVQ2my4pbA" data-csrf="true">
            </auto-check>
          </div>

          <div class="form-group">
            <label for="custom_scope_query">Query</label>
            <input type="text" name="custom_scope_query" id="custom_scope_query" data-target="custom-scopes.customScopesQueryField" class="form-control" autocomplete="off" placeholder="(repo:mona/a OR repo:mona/b) AND lang:python" required="" maxlength="500">
          </div>

          <p class="text-small color-fg-muted">
            To see all available qualifiers, see our <a class="Link--inTextBlock" href="https://docs.github.com/search-github/github-code-search/understanding-github-code-search-syntax">documentation</a>.
          </p>
</form>        </div>

        <div data-target="custom-scopes.manageCustomScopesForm">
          <div data-target="custom-scopes.list"></div>
        </div>

</div>
      </scrollable-region>
      <div data-view-component="true" class="Overlay-footer Overlay-footer--alignEnd Overlay-footer--divided">          <button data-action="click:custom-scopes#customScopesCancel" type="button" data-view-component="true" class="btn">    Cancel
</button>
          <button form="custom-scopes-dialog-form" data-action="click:custom-scopes#customScopesSubmit" data-target="custom-scopes.customScopesSubmitButton" type="submit" data-view-component="true" class="btn-primary btn">    Create saved search
</button>
</div>
</dialog></dialog-helper>
    </custom-scopes>
  </div>
</qbsearch-input>  <input type="hidden" value="Pnhqf26trRucG2NXFz5xXtt5YPX0OmzXKC-gygPccC8fBzn94zuYrRsvzDHFPcoGhEHu6_QcWNtV4sZLwHKavw" data-csrf="true" class="js-data-jump-to-suggestions-path-csrf">


          </div>

        
          <div class="AppHeader-CopilotChat hide-sm hide-md">
  <react-partial-anchor data-catalyst="">
      <a href="https://github.com/copilot" data-target="react-partial-anchor.anchor" id="copilot-chat-header-button" aria-labelledby="tooltip-676dd857-9ada-443e-97f2-612178e7f183" data-view-component="true" class="Button Button--iconOnly Button--secondary Button--medium AppHeader-button AppHeader-buttonLeft">  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-copilot Button-visual">
    <path d="M7.998 15.035c-4.562 0-7.873-2.914-7.998-3.749V9.338c.085-.628.677-1.686 1.588-2.065.013-.07.024-.143.036-.218.029-.183.06-.384.126-.612-.201-.508-.254-1.084-.254-1.656 0-.87.128-1.769.693-2.484.579-.733 1.494-1.124 2.724-1.261 1.206-.134 2.262.034 2.944.765.05.053.096.108.139.165.044-.057.094-.112.143-.165.682-.731 1.738-.899 2.944-.765 1.23.137 2.145.528 2.724 1.261.566.715.693 1.614.693 2.484 0 .572-.053 1.148-.254 1.656.066.228.098.429.126.612.012.076.024.148.037.218.924.385 1.522 1.471 1.591 2.095v1.872c0 .766-3.351 3.795-8.002 3.795Zm0-1.485c2.28 0 4.584-1.11 5.002-1.433V7.862l-.023-.116c-.49.21-1.075.291-1.727.291-1.146 0-2.059-.327-2.71-.991A3.222 3.222 0 0 1 8 6.303a3.24 3.24 0 0 1-.544.743c-.65.664-1.563.991-2.71.991-.652 0-1.236-.081-1.727-.291l-.023.116v4.255c.419.323 2.722 1.433 5.002 1.433ZM6.762 2.83c-.193-.206-.637-.413-1.682-.297-1.019.113-1.479.404-1.713.7-.247.312-.369.789-.369 1.554 0 .793.129 1.171.308 1.371.162.181.519.379 1.442.379.853 0 1.339-.235 1.638-.54.315-.322.527-.827.617-1.553.117-.935-.037-1.395-.241-1.614Zm4.155-.297c-1.044-.116-1.488.091-1.681.297-.204.219-.359.679-.242 1.614.091.726.303 1.231.618 1.553.299.305.784.54 1.638.54.922 0 1.28-.198 1.442-.379.179-.2.308-.578.308-1.371 0-.765-.123-1.242-.37-1.554-.233-.296-.693-.587-1.713-.7Z"></path><path d="M6.25 9.037a.75.75 0 0 1 .75.75v1.501a.75.75 0 0 1-1.5 0V9.787a.75.75 0 0 1 .75-.75Zm4.25.75v1.501a.75.75 0 0 1-1.5 0V9.787a.75.75 0 0 1 1.5 0Z"></path>
</svg>
</a><tool-tip id="tooltip-676dd857-9ada-443e-97f2-612178e7f183" for="copilot-chat-header-button" popover="manual" data-direction="s" data-type="label" data-view-component="true" class="sr-only position-absolute" aria-hidden="true" role="tooltip"><template shadowrootmode="open"><style>
      :host {
        --tooltip-top: var(--tool-tip-position-top, 0);
        --tooltip-left: var(--tool-tip-position-left, 0);
        padding: var(--overlay-paddingBlock-condensed) var(--overlay-padding-condensed) !important;
        font: var(--text-body-shorthand-small);
        color: var(--tooltip-fgColor, var(--fgColor-onEmphasis)) !important;
        text-align: center;
        text-decoration: none;
        text-shadow: none;
        text-transform: none;
        letter-spacing: normal;
        word-wrap: break-word;
        white-space: pre;
        background: var(--tooltip-bgColor, var(--bgColor-emphasis)) !important;
        border-radius: var(--borderRadius-medium);
        border: 0 !important;
        opacity: 0;
        max-width: var(--overlay-width-small);
        word-wrap: break-word;
        white-space: normal;
        width: max-content !important;
        inset: var(--tooltip-top) auto auto var(--tooltip-left) !important;
        overflow: visible !important;
        text-wrap: balance;
      }

      :host(:is(.tooltip-n, .tooltip-nw, .tooltip-ne)) {
        --tooltip-top: calc(var(--tool-tip-position-top, 0) - var(--overlay-offset, 0.25rem));
        --tooltip-left: var(--tool-tip-position-left);
      }

      :host(:is(.tooltip-s, .tooltip-sw, .tooltip-se)) {
        --tooltip-top: calc(var(--tool-tip-position-top, 0) + var(--overlay-offset, 0.25rem));
        --tooltip-left: var(--tool-tip-position-left);
      }

      :host(.tooltip-w) {
        --tooltip-top: var(--tool-tip-position-top);
        --tooltip-left: calc(var(--tool-tip-position-left, 0) - var(--overlay-offset, 0.25rem));
      }

      :host(.tooltip-e) {
        --tooltip-top: var(--tool-tip-position-top);
        --tooltip-left: calc(var(--tool-tip-position-left, 0) + var(--overlay-offset, 0.25rem));
      }

      :host:after{
        position: absolute;
        display: block;
        right: 0;
        left: 0;
        height: var(--overlay-offset, 0.25rem);
        content: "";
      }

      :host(.tooltip-s):after,
      :host(.tooltip-se):after,
      :host(.tooltip-sw):after {
        bottom: 100%
      }

      :host(.tooltip-n):after,
      :host(.tooltip-ne):after,
      :host(.tooltip-nw):after {
        top: 100%;
      }

      @keyframes tooltip-appear {
        from {
          opacity: 0;
        }
        to {
          opacity: 1;
        }
      }

      :host(:popover-open),
      :host(:popover-open):before {
        animation-name: tooltip-appear;
        animation-duration: .1s;
        animation-fill-mode: forwards;
        animation-timing-function: ease-in;
      }

      :host(.\:popover-open) {
        animation-name: tooltip-appear;
        animation-duration: .1s;
        animation-fill-mode: forwards;
        animation-timing-function: ease-in;
      }

      @media (forced-colors: active) {
        :host {
          outline: solid 1px transparent;
        }

        :host:before {
          display: none;
        }
      }
    </style><slot></slot></template>Chat with Copilot</tool-tip>

    
  
      <script crossorigin="anonymous" type="application/javascript" src="./app_files/vendors-node_modules_tanstack_query-core_build_modern_queryObserver_js-node_modules_tanstack_-defd52-0024bc0658ed.js.download" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="./app_files/vendors-node_modules_react-relay_index_js-a597b32944e2.js.download" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="./app_files/vendors-node_modules_remark-gfm_lib_index_js-node_modules_remark-parse_lib_index_js-node_modu-44d0fc-a919845a804c.js.download" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="./app_files/vendors-node_modules_hastscript_lib_index_js-node_modules_lowlight_lib_all_js-node_modules_re-713cc1-b7c90cd7720d.js.download" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="./app_files/vendors-node_modules_github_mini-throttle_dist_decorators_js-node_modules_accname_dist_access-690142-222222869963.js.download" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="./app_files/vendors-node_modules_focus-visible_dist_focus-visible_js-node_modules_github_hotkey_dist_inde-9239ad-9003aa70891d.js.download" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="./app_files/ui_packages_item-picker_components_RepositoryPicker_tsx-ui_packages_safe-html_SafeHTML_tsx-7f3b157d05b4.js.download" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="./app_files/ui_packages_copilot-chat_utils_copilot-chat-helpers_ts-6d6f969373ea.js.download" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="./app_files/ui_packages_copilot-markdown_MarkdownRenderer_tsx-085b7bc88355.js.download" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="./app_files/ui_packages_copilot-chat_utils_CopilotChatContext_tsx-055a28ee9a61.js.download" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="./app_files/ui_packages_copilot-chat_components_CopilotIconAnimation_tsx-ui_packages_copilot-chat_compone-8be2e4-63d882cd4d67.js.download" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="./app_files/copilot-chat-4fa9dc83b1f3.js.download" defer="defer"></script>
<link crossorigin="anonymous" media="all" rel="stylesheet" href="./app_files/primer-react.c212c596cc6bbefb1798.module.css">
<link crossorigin="anonymous" media="all" rel="stylesheet" href="./app_files/copilot-chat.2ae6ba95f674bcf88bc3.module.css">
      <link crossorigin="anonymous" media="all" rel="stylesheet" href="./app_files/copilot-markdown-rendering-f6845e8f5d6b.css">
      <script crossorigin="anonymous" type="application/javascript" src="./app_files/primer-react-957709c85fcc.js.download" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="./app_files/react-core-577edb5c37f8.js.download" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="./app_files/react-lib-8705026b409a.js.download" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="./app_files/octicons-react-9fd6ca6872cc.js.download" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="./app_files/vendors-node_modules_emotion_is-prop-valid_dist_emotion-is-prop-valid_esm_js-node_modules_emo-b1c483-b5947865157f.js.download" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="./app_files/vendors-ui_packages_react-router_node_modules_cookie_dist_index_js-node_modules_primer_live-r-4288ca-b9012d3355e6.js.download" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="./app_files/vendors-node_modules_tanstack_query-core_build_modern_queryObserver_js-node_modules_tanstack_-defd52-0024bc0658ed.js.download" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="./app_files/vendors-node_modules_react-relay_index_js-a597b32944e2.js.download" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="./app_files/vendors-node_modules_remark-gfm_lib_index_js-node_modules_remark-parse_lib_index_js-node_modu-44d0fc-a919845a804c.js.download" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="./app_files/vendors-node_modules_hastscript_lib_index_js-node_modules_lowlight_lib_all_js-node_modules_re-713cc1-b7c90cd7720d.js.download" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="./app_files/vendors-node_modules_github_mini-throttle_dist_decorators_js-node_modules_accname_dist_access-690142-222222869963.js.download" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="./app_files/vendors-node_modules_github_catalyst_lib_index_js-node_modules_github_hydro-analytics-client_-189aa3-aa0d1c491a18.js.download" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="./app_files/vendors-node_modules_focus-visible_dist_focus-visible_js-node_modules_github_hotkey_dist_inde-9239ad-9003aa70891d.js.download" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="./app_files/ui_packages_paths_index_ts-2c6108a4a75d.js.download" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="./app_files/ui_packages_ui-commands_ui-commands_ts-eb77c4447210.js.download" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="./app_files/ui_packages_item-picker_components_RepositoryPicker_tsx-ui_packages_safe-html_SafeHTML_tsx-7f3b157d05b4.js.download" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="./app_files/ui_packages_copilot-chat_utils_copilot-chat-helpers_ts-6d6f969373ea.js.download" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="./app_files/ui_packages_copilot-markdown_MarkdownRenderer_tsx-085b7bc88355.js.download" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="./app_files/ui_packages_copilot-chat_utils_CopilotChatContext_tsx-055a28ee9a61.js.download" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="./app_files/ui_packages_copilot-chat_components_CopilotIconAnimation_tsx-ui_packages_copilot-chat_compone-8be2e4-63d882cd4d67.js.download" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="./app_files/copilot-chat-4fa9dc83b1f3.js.download" defer="defer"></script>
<link crossorigin="anonymous" media="all" rel="stylesheet" href="./app_files/primer-react.c212c596cc6bbefb1798.module.css">
<link crossorigin="anonymous" media="all" rel="stylesheet" href="./app_files/copilot-chat.2ae6ba95f674bcf88bc3.module.css">

<react-partial partial-name="copilot-chat" data-ssr="false" data-attempted-ssr="false" data-react-profiling="false" data-catalyst="" class="loaded">
  
  <script type="application/json" data-target="react-partial.embeddedData">{"props":{"currentTopic":{"id":994512716,"name":"-Deploy_ke_Streamlit_Cloud","ownerLogin":"fastabyq","ownerType":"User","readmePath":"README.md","description":null,"commitOID":"da85b358297298a9cb40e00378ca9ef5d17989f3","ref":"refs/heads/main","refInfo":{"name":"main","type":"branch"},"visibility":"public","languages":[{"name":"Python","percent":100.0}],"customInstructions":[]},"findFileWorkerPath":"/assets-cdn/worker/find-file-worker-263cab1760dd.js","renderPopover":false,"renderBetaLabel":false,"chatIsVisible":true,"chatVisibleSettingPath":"/users/Jetgar/copilot_chat/settings/copilot_chat_visibility","ssoOrganizations":[],"apiVersion":"2025-05-01","agentsPath":"/github-copilot/chat/agents","apiURL":"https://api.individual.githubcopilot.com","currentUserLogin":"Jetgar","customInstructions":null,"renderKnowledgeBases":false,"customCopilotsEnabled":true,"optedInToPreviewFeatures":false,"optedInToUserFeedback":true,"renderAttachKnowledgeBaseHerePopover":true,"renderKnowledgeBaseAttachedToChatPopover":true,"personalInstructions":null,"reviewLab":false,"realIp":null,"scrollToTop":false,"hasCEorCBAccess":false,"licenseType":"licensed_limited","plan":null,"quotas":{"limits":{"chat":500,"completions":4000},"remaining":{"chat":500,"completions":4000},"resetDate":"2025-07-14","overagesEnabled":false},"icebreakers":[{"type":"functional","data":[{"id":"create-bug-issue","message":"Hi Copilot! Could you please start a draft issue for a bug? Once you've created the draft issue, if you need more information, ask me 1-2 key questions. If you also think I should upload any information or images that would help write the bug issue, let me know.","titleHtml":"Create an issue for a bug","icon":"issue-opened","color":"var(--display-green-fgColor)"},{"id":"summarize-pulls","message":"Hi Copilot! Could you help summarize a pull request? I'd like to know its purpose and the key changes made. Please include details about the problem it solves, new features or functionality introduced, any breaking changes, testing done, and documentation updates. Thank you!","titleHtml":"Summarize a pull request","icon":"git-pull-request","color":"var(--display-green-fgColor)"},{"id":"code-feedback","message":"Hi Copilot! Please review my code for best practices, readability, performance, and potential bugs. First, prompt me to provide the link to the relevant GitHub repository or file. Then, offer concrete suggestions for improvement, explain any issues you discover, and provide example corrections where appropriate.","titleHtml":"Get code feedback","icon":"code","color":"var(--display-gray-fgColor)"},{"id":"next-steps-issue","message":"Hi Copilot! Could you suggest the next actionable steps for an issue, based on either the provided issue link or a copy pasted description?","titleHtml":"Suggest next steps for an issue","icon":"issue-opened","color":"var(--display-green-fgColor)"},{"id":"understand-arch-diagram","message":"Hi Copilot! Could you please help me interpret this architecture diagram?","titleHtml":"Interpret an architecture diagram","icon":"eye","color":"var(--display-purple-fgColor)"},{"id":"create-profile-readme","message":"Hi Copilot! Please create a standout profile README for $$USERNAME$$. Ask me for any key details (such as my profession, top skills, favorite projects, or social links) that would help you personalize it.","titleHtml":"Create a profile README for me","icon":"rocket","color":"var(--display-pink-fgColor)"},{"id":"my-open-pulls","message":"Hi Copilot! Can you please find my open pull requests?","titleHtml":"My open pull requests","icon":"git-pull-request","color":"var(--display-green-fgColor)"},{"id":"make-pong","message":"Hi Copilot! Could you generate a simple Pong game utilizing HTML, CSS, and JavaScript? The player should control the left paddle with their mouse, and the right paddle should be controlled automatically by a basic AI. Make sure the game includes a bouncing ball and collision detection for paddles and walls. Please provide the code for all three components: the HTML file, the CSS file, and the JavaScript file directly within the chat window. Thanks!","titleHtml":"Make a Pong game","icon":"code","color":"var(--display-gray-fgColor)"}]},{"type":"instructional","data":[]},{"type":"interactional","data":[{"id":"to-do-app-local-storage","message":"Create a to-do list application with local storage functionality.","titleHtml":"To-do list with local storage","icon":"code","color":"var(--display-gray-fgColor)"},{"id":"digital-clock-time-zones","message":"Create a digital clock that displays the current time in different time zones.","titleHtml":"A digital time zone clock","icon":"code","color":"var(--display-gray-fgColor)"},{"id":"weather-dashboard-app","message":"Develop a weather dashboard that fetches data from a public weather API.","titleHtml":"Develop a weather dashboard","icon":"code","color":"var(--display-gray-fgColor)"},{"id":"create-joke-generator","message":"Create a random joke generator using an external API.","titleHtml":"Create a joke generator","icon":"code","color":"var(--display-gray-fgColor)"}]}],"canShareThread":true}}</script>
  <div data-target="react-partial.reactRoot"><div class="Box-sc-g0xbh4-0 bpDFns"></div><div class="Box-sc-g0xbh4-0 hmHhrt"></div><script type="application/json" id="__PRIMER_DATA_:r1q:__">{"resolvedServerColorMode":"night"}</script></div>
</react-partial>


    </react-partial-anchor>
  <react-partial-anchor data-catalyst="">
    <button id="global-copilot-menu-button" data-target="react-partial-anchor.anchor" aria-expanded="false" aria-labelledby="tooltip-ebf45503-c9ed-48d2-a1f0-378b8fb771cd" type="button" data-view-component="true" class="Button Button--iconOnly Button--secondary Button--medium AppHeader-button AppHeader-buttonRight" aria-haspopup="true">  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-triangle-down Button-visual">
    <path d="m4.427 7.427 3.396 3.396a.25.25 0 0 0 .354 0l3.396-3.396A.25.25 0 0 0 11.396 7H4.604a.25.25 0 0 0-.177.427Z"></path>
</svg>
</button><tool-tip id="tooltip-ebf45503-c9ed-48d2-a1f0-378b8fb771cd" for="global-copilot-menu-button" popover="manual" data-direction="s" data-type="label" data-view-component="true" class="sr-only position-absolute" aria-hidden="true" role="tooltip"><template shadowrootmode="open"><style>
      :host {
        --tooltip-top: var(--tool-tip-position-top, 0);
        --tooltip-left: var(--tool-tip-position-left, 0);
        padding: var(--overlay-paddingBlock-condensed) var(--overlay-padding-condensed) !important;
        font: var(--text-body-shorthand-small);
        color: var(--tooltip-fgColor, var(--fgColor-onEmphasis)) !important;
        text-align: center;
        text-decoration: none;
        text-shadow: none;
        text-transform: none;
        letter-spacing: normal;
        word-wrap: break-word;
        white-space: pre;
        background: var(--tooltip-bgColor, var(--bgColor-emphasis)) !important;
        border-radius: var(--borderRadius-medium);
        border: 0 !important;
        opacity: 0;
        max-width: var(--overlay-width-small);
        word-wrap: break-word;
        white-space: normal;
        width: max-content !important;
        inset: var(--tooltip-top) auto auto var(--tooltip-left) !important;
        overflow: visible !important;
        text-wrap: balance;
      }

      :host(:is(.tooltip-n, .tooltip-nw, .tooltip-ne)) {
        --tooltip-top: calc(var(--tool-tip-position-top, 0) - var(--overlay-offset, 0.25rem));
        --tooltip-left: var(--tool-tip-position-left);
      }

      :host(:is(.tooltip-s, .tooltip-sw, .tooltip-se)) {
        --tooltip-top: calc(var(--tool-tip-position-top, 0) + var(--overlay-offset, 0.25rem));
        --tooltip-left: var(--tool-tip-position-left);
      }

      :host(.tooltip-w) {
        --tooltip-top: var(--tool-tip-position-top);
        --tooltip-left: calc(var(--tool-tip-position-left, 0) - var(--overlay-offset, 0.25rem));
      }

      :host(.tooltip-e) {
        --tooltip-top: var(--tool-tip-position-top);
        --tooltip-left: calc(var(--tool-tip-position-left, 0) + var(--overlay-offset, 0.25rem));
      }

      :host:after{
        position: absolute;
        display: block;
        right: 0;
        left: 0;
        height: var(--overlay-offset, 0.25rem);
        content: "";
      }

      :host(.tooltip-s):after,
      :host(.tooltip-se):after,
      :host(.tooltip-sw):after {
        bottom: 100%
      }

      :host(.tooltip-n):after,
      :host(.tooltip-ne):after,
      :host(.tooltip-nw):after {
        top: 100%;
      }

      @keyframes tooltip-appear {
        from {
          opacity: 0;
        }
        to {
          opacity: 1;
        }
      }

      :host(:popover-open),
      :host(:popover-open):before {
        animation-name: tooltip-appear;
        animation-duration: .1s;
        animation-fill-mode: forwards;
        animation-timing-function: ease-in;
      }

      :host(.\:popover-open) {
        animation-name: tooltip-appear;
        animation-duration: .1s;
        animation-fill-mode: forwards;
        animation-timing-function: ease-in;
      }

      @media (forced-colors: active) {
        :host {
          outline: solid 1px transparent;
        }

        :host:before {
          display: none;
        }
      }
    </style><slot></slot></template>Open Copilot…</tool-tip>

    
  
      <script crossorigin="anonymous" type="application/javascript" src="./app_files/global-copilot-menu-e4af1f6d8af8.js.download" defer="defer"></script>
<link crossorigin="anonymous" media="all" rel="stylesheet" href="./app_files/primer-react.c212c596cc6bbefb1798.module.css">
<link crossorigin="anonymous" media="all" rel="stylesheet" href="./app_files/global-copilot-menu.972c8de5acbdcb17b799.module.css">

<react-partial partial-name="global-copilot-menu" data-ssr="false" data-attempted-ssr="false" data-react-profiling="false" data-catalyst="" class="loaded">
  
  <script type="application/json" data-target="react-partial.embeddedData">{"props":{}}</script>
  <div data-target="react-partial.reactRoot"><div class="d-none"></div><script type="application/json" id="__PRIMER_DATA_:r1g:__">{"resolvedServerColorMode":"night"}</script></div>
</react-partial>

    </react-partial-anchor>
</div>


        <div class="AppHeader-actions position-relative">
             <react-partial-anchor data-catalyst="">
      <button id="global-create-menu-anchor" aria-label="Create something new" data-target="react-partial-anchor.anchor" type="button" data-view-component="true" class="AppHeader-button global-create-button Button--secondary Button--medium Button width-auto color-fg-muted" aria-describedby="tooltip-c2d057b3-f0bf-473f-bf62-31bf4f89b9bf" aria-expanded="false" aria-haspopup="true">  <span class="Button-content">
      <span class="Button-visual Button-leadingVisual">
        <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
      </span>
    <span class="Button-label"><svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-triangle-down">
    <path d="m4.427 7.427 3.396 3.396a.25.25 0 0 0 .354 0l3.396-3.396A.25.25 0 0 0 11.396 7H4.604a.25.25 0 0 0-.177.427Z"></path>
</svg></span>
  </span>
</button><tool-tip id="tooltip-c2d057b3-f0bf-473f-bf62-31bf4f89b9bf" for="global-create-menu-anchor" popover="manual" data-direction="s" data-type="description" data-view-component="true" class="sr-only position-absolute" role="tooltip"><template shadowrootmode="open"><style>
      :host {
        --tooltip-top: var(--tool-tip-position-top, 0);
        --tooltip-left: var(--tool-tip-position-left, 0);
        padding: var(--overlay-paddingBlock-condensed) var(--overlay-padding-condensed) !important;
        font: var(--text-body-shorthand-small);
        color: var(--tooltip-fgColor, var(--fgColor-onEmphasis)) !important;
        text-align: center;
        text-decoration: none;
        text-shadow: none;
        text-transform: none;
        letter-spacing: normal;
        word-wrap: break-word;
        white-space: pre;
        background: var(--tooltip-bgColor, var(--bgColor-emphasis)) !important;
        border-radius: var(--borderRadius-medium);
        border: 0 !important;
        opacity: 0;
        max-width: var(--overlay-width-small);
        word-wrap: break-word;
        white-space: normal;
        width: max-content !important;
        inset: var(--tooltip-top) auto auto var(--tooltip-left) !important;
        overflow: visible !important;
        text-wrap: balance;
      }

      :host(:is(.tooltip-n, .tooltip-nw, .tooltip-ne)) {
        --tooltip-top: calc(var(--tool-tip-position-top, 0) - var(--overlay-offset, 0.25rem));
        --tooltip-left: var(--tool-tip-position-left);
      }

      :host(:is(.tooltip-s, .tooltip-sw, .tooltip-se)) {
        --tooltip-top: calc(var(--tool-tip-position-top, 0) + var(--overlay-offset, 0.25rem));
        --tooltip-left: var(--tool-tip-position-left);
      }

      :host(.tooltip-w) {
        --tooltip-top: var(--tool-tip-position-top);
        --tooltip-left: calc(var(--tool-tip-position-left, 0) - var(--overlay-offset, 0.25rem));
      }

      :host(.tooltip-e) {
        --tooltip-top: var(--tool-tip-position-top);
        --tooltip-left: calc(var(--tool-tip-position-left, 0) + var(--overlay-offset, 0.25rem));
      }

      :host:after{
        position: absolute;
        display: block;
        right: 0;
        left: 0;
        height: var(--overlay-offset, 0.25rem);
        content: "";
      }

      :host(.tooltip-s):after,
      :host(.tooltip-se):after,
      :host(.tooltip-sw):after {
        bottom: 100%
      }

      :host(.tooltip-n):after,
      :host(.tooltip-ne):after,
      :host(.tooltip-nw):after {
        top: 100%;
      }

      @keyframes tooltip-appear {
        from {
          opacity: 0;
        }
        to {
          opacity: 1;
        }
      }

      :host(:popover-open),
      :host(:popover-open):before {
        animation-name: tooltip-appear;
        animation-duration: .1s;
        animation-fill-mode: forwards;
        animation-timing-function: ease-in;
      }

      :host(.\:popover-open) {
        animation-name: tooltip-appear;
        animation-duration: .1s;
        animation-fill-mode: forwards;
        animation-timing-function: ease-in;
      }

      @media (forced-colors: active) {
        :host {
          outline: solid 1px transparent;
        }

        :host:before {
          display: none;
        }
      }
    </style><slot></slot></template>Create new...</tool-tip>

      
    
        <script crossorigin="anonymous" type="application/javascript" src="./app_files/vendors-node_modules_github_catalyst_lib_index_js-node_modules_github_hydro-analytics-client_-4da1df-de7253948a7c.js.download" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="./app_files/ui_packages_document-metadata_document-metadata_ts-ui_packages_promise-with-resolvers-polyfil-b81d9e-bf9e0c14eede.js.download" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="./app_files/global-create-menu-25d44959288c.js.download" defer="defer"></script>
<link crossorigin="anonymous" media="all" rel="stylesheet" href="./app_files/primer-react.c212c596cc6bbefb1798.module.css">
<link crossorigin="anonymous" media="all" rel="stylesheet" href="./app_files/global-create-menu.b1ee6a6bae56a89148b1.module.css">

<react-partial partial-name="global-create-menu" data-ssr="false" data-attempted-ssr="false" data-react-profiling="false" data-catalyst="" class="loaded">
  
  <script type="application/json" data-target="react-partial.embeddedData">{"props":{"createRepo":true,"importRepo":true,"codespaces":true,"spark":false,"gist":true,"createOrg":true,"createProject":false,"createProjectUrl":"/Jetgar?tab=projects","createLegacyProject":false,"createIssue":false,"org":null,"owner":"fastabyq","repo":"-Deploy_ke_Streamlit_Cloud"}}</script>
  <div data-target="react-partial.reactRoot"><script type="application/json" id="__PRIMER_DATA_:r1k:__">{"resolvedServerColorMode":"night"}</script></div>
</react-partial>

      </react-partial-anchor>


            <a href="https://github.com/issues" data-analytics-event="{&quot;category&quot;:&quot;Global navigation&quot;,&quot;action&quot;:&quot;ISSUES_HEADER&quot;,&quot;label&quot;:null}" id="icon-button-a7779f6c-25f4-43e0-99ed-a906f3b3585b" aria-labelledby="tooltip-3dd50132-76db-4a8a-88b7-f461ba9d7d7e" data-view-component="true" class="Button Button--iconOnly Button--secondary Button--medium AppHeader-button color-fg-muted">  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-issue-opened Button-visual">
    <path d="M8 9.5a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3Z"></path><path d="M8 0a8 8 0 1 1 0 16A8 8 0 0 1 8 0ZM1.5 8a6.5 6.5 0 1 0 13 0 6.5 6.5 0 0 0-13 0Z"></path>
</svg>
</a><tool-tip id="tooltip-3dd50132-76db-4a8a-88b7-f461ba9d7d7e" for="icon-button-a7779f6c-25f4-43e0-99ed-a906f3b3585b" popover="manual" data-direction="s" data-type="label" data-view-component="true" class="sr-only position-absolute" aria-hidden="true" role="tooltip"><template shadowrootmode="open"><style>
      :host {
        --tooltip-top: var(--tool-tip-position-top, 0);
        --tooltip-left: var(--tool-tip-position-left, 0);
        padding: var(--overlay-paddingBlock-condensed) var(--overlay-padding-condensed) !important;
        font: var(--text-body-shorthand-small);
        color: var(--tooltip-fgColor, var(--fgColor-onEmphasis)) !important;
        text-align: center;
        text-decoration: none;
        text-shadow: none;
        text-transform: none;
        letter-spacing: normal;
        word-wrap: break-word;
        white-space: pre;
        background: var(--tooltip-bgColor, var(--bgColor-emphasis)) !important;
        border-radius: var(--borderRadius-medium);
        border: 0 !important;
        opacity: 0;
        max-width: var(--overlay-width-small);
        word-wrap: break-word;
        white-space: normal;
        width: max-content !important;
        inset: var(--tooltip-top) auto auto var(--tooltip-left) !important;
        overflow: visible !important;
        text-wrap: balance;
      }

      :host(:is(.tooltip-n, .tooltip-nw, .tooltip-ne)) {
        --tooltip-top: calc(var(--tool-tip-position-top, 0) - var(--overlay-offset, 0.25rem));
        --tooltip-left: var(--tool-tip-position-left);
      }

      :host(:is(.tooltip-s, .tooltip-sw, .tooltip-se)) {
        --tooltip-top: calc(var(--tool-tip-position-top, 0) + var(--overlay-offset, 0.25rem));
        --tooltip-left: var(--tool-tip-position-left);
      }

      :host(.tooltip-w) {
        --tooltip-top: var(--tool-tip-position-top);
        --tooltip-left: calc(var(--tool-tip-position-left, 0) - var(--overlay-offset, 0.25rem));
      }

      :host(.tooltip-e) {
        --tooltip-top: var(--tool-tip-position-top);
        --tooltip-left: calc(var(--tool-tip-position-left, 0) + var(--overlay-offset, 0.25rem));
      }

      :host:after{
        position: absolute;
        display: block;
        right: 0;
        left: 0;
        height: var(--overlay-offset, 0.25rem);
        content: "";
      }

      :host(.tooltip-s):after,
      :host(.tooltip-se):after,
      :host(.tooltip-sw):after {
        bottom: 100%
      }

      :host(.tooltip-n):after,
      :host(.tooltip-ne):after,
      :host(.tooltip-nw):after {
        top: 100%;
      }

      @keyframes tooltip-appear {
        from {
          opacity: 0;
        }
        to {
          opacity: 1;
        }
      }

      :host(:popover-open),
      :host(:popover-open):before {
        animation-name: tooltip-appear;
        animation-duration: .1s;
        animation-fill-mode: forwards;
        animation-timing-function: ease-in;
      }

      :host(.\:popover-open) {
        animation-name: tooltip-appear;
        animation-duration: .1s;
        animation-fill-mode: forwards;
        animation-timing-function: ease-in;
      }

      @media (forced-colors: active) {
        :host {
          outline: solid 1px transparent;
        }

        :host:before {
          display: none;
        }
      }
    </style><slot></slot></template>Your issues</tool-tip>

            <a href="https://github.com/pulls" data-analytics-event="{&quot;category&quot;:&quot;Global navigation&quot;,&quot;action&quot;:&quot;PULL_REQUESTS_HEADER&quot;,&quot;label&quot;:null}" id="icon-button-ddb02bae-cbf7-49a6-a74c-32e46fbfd88e" aria-labelledby="tooltip-8e404170-1d61-4a27-958e-ef85e6b2ae17" data-view-component="true" class="Button Button--iconOnly Button--secondary Button--medium AppHeader-button color-fg-muted">  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-git-pull-request Button-visual">
    <path d="M1.5 3.25a2.25 2.25 0 1 1 3 2.122v5.256a2.251 2.251 0 1 1-1.5 0V5.372A2.25 2.25 0 0 1 1.5 3.25Zm5.677-.177L9.573.677A.25.25 0 0 1 10 .854V2.5h1A2.5 2.5 0 0 1 13.5 5v5.628a2.251 2.251 0 1 1-1.5 0V5a1 1 0 0 0-1-1h-1v1.646a.25.25 0 0 1-.427.177L7.177 3.427a.25.25 0 0 1 0-.354ZM3.75 2.5a.75.75 0 1 0 0 1.5.75.75 0 0 0 0-1.5Zm0 9.5a.75.75 0 1 0 0 1.5.75.75 0 0 0 0-1.5Zm8.25.75a.75.75 0 1 0 1.5 0 .75.75 0 0 0-1.5 0Z"></path>
</svg>
</a><tool-tip id="tooltip-8e404170-1d61-4a27-958e-ef85e6b2ae17" for="icon-button-ddb02bae-cbf7-49a6-a74c-32e46fbfd88e" popover="manual" data-direction="s" data-type="label" data-view-component="true" class="sr-only position-absolute" aria-hidden="true" role="tooltip"><template shadowrootmode="open"><style>
      :host {
        --tooltip-top: var(--tool-tip-position-top, 0);
        --tooltip-left: var(--tool-tip-position-left, 0);
        padding: var(--overlay-paddingBlock-condensed) var(--overlay-padding-condensed) !important;
        font: var(--text-body-shorthand-small);
        color: var(--tooltip-fgColor, var(--fgColor-onEmphasis)) !important;
        text-align: center;
        text-decoration: none;
        text-shadow: none;
        text-transform: none;
        letter-spacing: normal;
        word-wrap: break-word;
        white-space: pre;
        background: var(--tooltip-bgColor, var(--bgColor-emphasis)) !important;
        border-radius: var(--borderRadius-medium);
        border: 0 !important;
        opacity: 0;
        max-width: var(--overlay-width-small);
        word-wrap: break-word;
        white-space: normal;
        width: max-content !important;
        inset: var(--tooltip-top) auto auto var(--tooltip-left) !important;
        overflow: visible !important;
        text-wrap: balance;
      }

      :host(:is(.tooltip-n, .tooltip-nw, .tooltip-ne)) {
        --tooltip-top: calc(var(--tool-tip-position-top, 0) - var(--overlay-offset, 0.25rem));
        --tooltip-left: var(--tool-tip-position-left);
      }

      :host(:is(.tooltip-s, .tooltip-sw, .tooltip-se)) {
        --tooltip-top: calc(var(--tool-tip-position-top, 0) + var(--overlay-offset, 0.25rem));
        --tooltip-left: var(--tool-tip-position-left);
      }

      :host(.tooltip-w) {
        --tooltip-top: var(--tool-tip-position-top);
        --tooltip-left: calc(var(--tool-tip-position-left, 0) - var(--overlay-offset, 0.25rem));
      }

      :host(.tooltip-e) {
        --tooltip-top: var(--tool-tip-position-top);
        --tooltip-left: calc(var(--tool-tip-position-left, 0) + var(--overlay-offset, 0.25rem));
      }

      :host:after{
        position: absolute;
        display: block;
        right: 0;
        left: 0;
        height: var(--overlay-offset, 0.25rem);
        content: "";
      }

      :host(.tooltip-s):after,
      :host(.tooltip-se):after,
      :host(.tooltip-sw):after {
        bottom: 100%
      }

      :host(.tooltip-n):after,
      :host(.tooltip-ne):after,
      :host(.tooltip-nw):after {
        top: 100%;
      }

      @keyframes tooltip-appear {
        from {
          opacity: 0;
        }
        to {
          opacity: 1;
        }
      }

      :host(:popover-open),
      :host(:popover-open):before {
        animation-name: tooltip-appear;
        animation-duration: .1s;
        animation-fill-mode: forwards;
        animation-timing-function: ease-in;
      }

      :host(.\:popover-open) {
        animation-name: tooltip-appear;
        animation-duration: .1s;
        animation-fill-mode: forwards;
        animation-timing-function: ease-in;
      }

      @media (forced-colors: active) {
        :host {
          outline: solid 1px transparent;
        }

        :host:before {
          display: none;
        }
      }
    </style><slot></slot></template>Your pull requests</tool-tip>

        </div>

          <notification-indicator data-channel="eyJjIjoibm90aWZpY2F0aW9uLWNoYW5nZWQ6MTI4MTMwMzQ3IiwidCI6MTc1MDA2Mjg0N30=--c6e3ea4ddf03c8b6f396e3e81b0291b4a0579d7c57f1bd444a725f44337f7b3c" data-indicator-mode="none" data-tooltip-global="You have unread notifications" data-tooltip-unavailable="Notifications are unavailable at the moment." data-tooltip-none="You have no unread notifications" data-header-redesign-enabled="true" data-fetch-indicator-src="/notifications/indicator" data-fetch-indicator-enabled="true" data-view-component="true" class="js-socket-channel" data-fetch-retry-delay-time="500" data-catalyst="">
    <a id="AppHeader-notifications-button" href="https://github.com/notifications" aria-labelledby="notification-indicator-tooltip" data-hotkey="g n" data-target="notification-indicator.link" data-analytics-event="{&quot;category&quot;:&quot;Global navigation&quot;,&quot;action&quot;:&quot;NOTIFICATIONS_HEADER&quot;,&quot;label&quot;:&quot;icon:read&quot;}" data-view-component="true" class="Button Button--iconOnly Button--secondary Button--medium AppHeader-button color-fg-muted">  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-inbox Button-visual">
    <path d="M2.8 2.06A1.75 1.75 0 0 1 4.41 1h7.18c.7 0 1.333.417 1.61 1.06l2.74 6.395c.04.093.06.194.06.295v4.5A1.75 1.75 0 0 1 14.25 15H1.75A1.75 1.75 0 0 1 0 13.25v-4.5c0-.101.02-.202.06-.295Zm1.61.44a.25.25 0 0 0-.23.152L1.887 8H4.75a.75.75 0 0 1 .6.3L6.625 10h2.75l1.275-1.7a.75.75 0 0 1 .6-.3h2.863L11.82 2.652a.25.25 0 0 0-.23-.152Zm10.09 7h-2.875l-1.275 1.7a.75.75 0 0 1-.6.3h-3.5a.75.75 0 0 1-.6-.3L4.375 9.5H1.5v3.75c0 .138.112.25.25.25h12.5a.25.25 0 0 0 .25-.25Z"></path>
</svg>
</a>

    <tool-tip id="notification-indicator-tooltip" data-target="notification-indicator.tooltip" for="AppHeader-notifications-button" popover="manual" data-direction="s" data-type="label" data-view-component="true" class="sr-only position-absolute" aria-hidden="true" role="tooltip"><template shadowrootmode="open"><style>
      :host {
        --tooltip-top: var(--tool-tip-position-top, 0);
        --tooltip-left: var(--tool-tip-position-left, 0);
        padding: var(--overlay-paddingBlock-condensed) var(--overlay-padding-condensed) !important;
        font: var(--text-body-shorthand-small);
        color: var(--tooltip-fgColor, var(--fgColor-onEmphasis)) !important;
        text-align: center;
        text-decoration: none;
        text-shadow: none;
        text-transform: none;
        letter-spacing: normal;
        word-wrap: break-word;
        white-space: pre;
        background: var(--tooltip-bgColor, var(--bgColor-emphasis)) !important;
        border-radius: var(--borderRadius-medium);
        border: 0 !important;
        opacity: 0;
        max-width: var(--overlay-width-small);
        word-wrap: break-word;
        white-space: normal;
        width: max-content !important;
        inset: var(--tooltip-top) auto auto var(--tooltip-left) !important;
        overflow: visible !important;
        text-wrap: balance;
      }

      :host(:is(.tooltip-n, .tooltip-nw, .tooltip-ne)) {
        --tooltip-top: calc(var(--tool-tip-position-top, 0) - var(--overlay-offset, 0.25rem));
        --tooltip-left: var(--tool-tip-position-left);
      }

      :host(:is(.tooltip-s, .tooltip-sw, .tooltip-se)) {
        --tooltip-top: calc(var(--tool-tip-position-top, 0) + var(--overlay-offset, 0.25rem));
        --tooltip-left: var(--tool-tip-position-left);
      }

      :host(.tooltip-w) {
        --tooltip-top: var(--tool-tip-position-top);
        --tooltip-left: calc(var(--tool-tip-position-left, 0) - var(--overlay-offset, 0.25rem));
      }

      :host(.tooltip-e) {
        --tooltip-top: var(--tool-tip-position-top);
        --tooltip-left: calc(var(--tool-tip-position-left, 0) + var(--overlay-offset, 0.25rem));
      }

      :host:after{
        position: absolute;
        display: block;
        right: 0;
        left: 0;
        height: var(--overlay-offset, 0.25rem);
        content: "";
      }

      :host(.tooltip-s):after,
      :host(.tooltip-se):after,
      :host(.tooltip-sw):after {
        bottom: 100%
      }

      :host(.tooltip-n):after,
      :host(.tooltip-ne):after,
      :host(.tooltip-nw):after {
        top: 100%;
      }

      @keyframes tooltip-appear {
        from {
          opacity: 0;
        }
        to {
          opacity: 1;
        }
      }

      :host(:popover-open),
      :host(:popover-open):before {
        animation-name: tooltip-appear;
        animation-duration: .1s;
        animation-fill-mode: forwards;
        animation-timing-function: ease-in;
      }

      :host(.\:popover-open) {
        animation-name: tooltip-appear;
        animation-duration: .1s;
        animation-fill-mode: forwards;
        animation-timing-function: ease-in;
      }

      @media (forced-colors: active) {
        :host {
          outline: solid 1px transparent;
        }

        :host:before {
          display: none;
        }
      }
    </style><slot></slot></template>You have no unread notifications</tool-tip>
</notification-indicator>

        <div class="AppHeader-user">
          <deferred-side-panel data-url="/_side-panels/user?repository_id=994512716" data-catalyst="">
  <include-fragment data-target="deferred-side-panel.fragment" data-nonce="v2:fac17c6a-5a3e-3145-7e99-dbeb3ad3f493" data-view-component="true"><template shadowrootmode="open"><style>:host {display: block;}</style><slot></slot></template>
  
    <react-partial-anchor data-catalyst="">
  <button data-target="react-partial-anchor.anchor" data-login="Jetgar" aria-label="Open user navigation menu" type="button" data-view-component="true" class="Button--invisible Button--medium Button Button--invisible-noVisuals color-bg-transparent p-0" aria-expanded="false" aria-haspopup="true">  <span class="Button-content">
    <span class="Button-label"><img src="./app_files/128130347" alt="" size="32" height="32" width="32" data-view-component="true" class="avatar circle"></span>
  </span>
</button>
  

    <script crossorigin="anonymous" type="application/javascript" src="./app_files/global-user-nav-drawer-43e174f4fe91.js.download" defer="defer"></script>
<link crossorigin="anonymous" media="all" rel="stylesheet" href="./app_files/primer-react.c212c596cc6bbefb1798.module.css">
<link crossorigin="anonymous" media="all" rel="stylesheet" href="./app_files/global-user-nav-drawer.f5c870dfa3e88b836b2b.module.css">

<react-partial partial-name="global-user-nav-drawer" data-ssr="false" data-attempted-ssr="false" data-react-profiling="false" data-catalyst="" class="loaded">
  
  <script type="application/json" data-target="react-partial.embeddedData">{"props":{"owner":{"login":"Jetgar","name":null,"avatarUrl":"https://avatars.githubusercontent.com/u/128130347?v=4"},"drawerId":"global-user-nav-drawer","lazyLoadItemDataFetchUrl":"/_side-panels/user.json","canAddAccount":true,"addAccountPath":"/login?add_account=1\u0026return_to=https%3A%2F%2Fgithub.com%2Ffastabyq%2F-Deploy_ke_Streamlit_Cloud%2Fblob%2Fmain%2Fapp.py","switchAccountPath":"/switch_account","loginAccountPath":"/login?add_account=1","projectsPath":"/Jetgar?tab=projects","gistsUrl":"https://gist.github.com/mine","docsUrl":"https://docs.github.com","yourEnterpriseUrl":null,"enterpriseSettingsUrl":null,"supportUrl":"https://support.github.com","showAccountSwitcher":true,"showCopilot":true,"showEnterprises":true,"showEnterprise":false,"showGists":true,"showOrganizations":true,"showSponsors":true,"showUpgrade":true,"showFeaturesPreviews":true,"showEnterpriseSettings":false,"createMenuProps":{"createRepo":true,"importRepo":true,"codespaces":true,"spark":false,"gist":true,"createOrg":true,"createProject":false,"createProjectUrl":"/Jetgar?tab=projects","createLegacyProject":false,"createIssue":false,"org":null,"owner":"fastabyq","repo":"-Deploy_ke_Streamlit_Cloud"}}}</script>
  <div data-target="react-partial.reactRoot"><script type="application/json" id="__PRIMER_DATA_:r1n:__">{"resolvedServerColorMode":"night"}</script></div>
</react-partial>

  </react-partial-anchor>


  <div data-show-on-forbidden-error="" hidden="">
    <div class="Box">
  <div class="blankslate-container">
    <div data-view-component="true" class="blankslate blankslate-spacious color-bg-default rounded-2">
      

      <h3 data-view-component="true" class="blankslate-heading">        Uh oh!
</h3>
      <p data-view-component="true">        </p><p class="color-fg-muted my-2 mb-2 ws-normal">There was an error while loading. <a class="Link--inTextBlock" data-turbo="false" href="https://github.com/fastabyq/-Deploy_ke_Streamlit_Cloud/blob/main/app.py" aria-label="Please reload this page">Please reload this page</a>.</p>
<p></p>

</div>  </div>
</div>  </div>
</include-fragment></deferred-side-panel>
        </div>

        <div class="position-absolute mt-2">
            
<site-header-logged-in-user-menu data-catalyst="">

</site-header-logged-in-user-menu>

        </div>
      </div>
    </div>


    
        <div class="AppHeader-localBar">
          <nav data-pjax="#js-repo-pjax-container" aria-label="Repository" data-view-component="true" class="js-repo-nav js-sidenav-container-pjax js-responsive-underlinenav overflow-hidden UnderlineNav">

  <ul data-view-component="true" class="UnderlineNav-body list-style-none">
      <li data-view-component="true" class="d-inline-flex">
  <a id="code-tab" href="https://github.com/fastabyq/-Deploy_ke_Streamlit_Cloud" data-tab-item="i0code-tab" data-selected-links="repo_source repo_downloads repo_commits repo_releases repo_tags repo_branches repo_packages repo_deployments repo_attestations /fastabyq/-Deploy_ke_Streamlit_Cloud" data-pjax="#repo-content-pjax-container" data-turbo-frame="repo-content-turbo-frame" data-hotkey="g c" data-analytics-event="{&quot;category&quot;:&quot;Underline navbar&quot;,&quot;action&quot;:&quot;Click tab&quot;,&quot;label&quot;:&quot;Code&quot;,&quot;target&quot;:&quot;UNDERLINE_NAV.TAB&quot;}" data-view-component="true" class="UnderlineNav-item no-wrap js-responsive-underlinenav-item js-selected-navigation-item selected" aria-current="page">
    
              <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-code UnderlineNav-octicon d-none d-sm-inline">
    <path d="m11.28 3.22 4.25 4.25a.75.75 0 0 1 0 1.06l-4.25 4.25a.749.749 0 0 1-1.275-.326.749.749 0 0 1 .215-.734L13.94 8l-3.72-3.72a.749.749 0 0 1 .326-1.275.749.749 0 0 1 .734.215Zm-6.56 0a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042L2.06 8l3.72 3.72a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215L.47 8.53a.75.75 0 0 1 0-1.06Z"></path>
</svg>
        <span data-content="Code">Code</span>
          <span id="code-repo-tab-count" data-pjax-replace="" data-turbo-replace="" title="Not available" data-view-component="true" class="Counter"></span>


    
</a></li>
      <li data-view-component="true" class="d-inline-flex">
  <a id="issues-tab" href="https://github.com/fastabyq/-Deploy_ke_Streamlit_Cloud/issues" data-tab-item="i1issues-tab" data-selected-links="repo_issues repo_labels repo_milestones /fastabyq/-Deploy_ke_Streamlit_Cloud/issues" data-pjax="#repo-content-pjax-container" data-turbo-frame="repo-content-turbo-frame" data-hotkey="g i" data-analytics-event="{&quot;category&quot;:&quot;Underline navbar&quot;,&quot;action&quot;:&quot;Click tab&quot;,&quot;label&quot;:&quot;Issues&quot;,&quot;target&quot;:&quot;UNDERLINE_NAV.TAB&quot;}" data-view-component="true" class="UnderlineNav-item no-wrap js-responsive-underlinenav-item js-selected-navigation-item">
    
              <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-issue-opened UnderlineNav-octicon d-none d-sm-inline">
    <path d="M8 9.5a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3Z"></path><path d="M8 0a8 8 0 1 1 0 16A8 8 0 0 1 8 0ZM1.5 8a6.5 6.5 0 1 0 13 0 6.5 6.5 0 0 0-13 0Z"></path>
</svg>
        <span data-content="Issues">Issues</span>
          <span id="issues-repo-tab-count" data-pjax-replace="" data-turbo-replace="" title="0" hidden="hidden" data-view-component="true" class="Counter">0</span>


    
</a></li>
      <li data-view-component="true" class="d-inline-flex">
  <a id="pull-requests-tab" href="https://github.com/fastabyq/-Deploy_ke_Streamlit_Cloud/pulls" data-tab-item="i2pull-requests-tab" data-selected-links="repo_pulls checks /fastabyq/-Deploy_ke_Streamlit_Cloud/pulls" data-pjax="#repo-content-pjax-container" data-turbo-frame="repo-content-turbo-frame" data-hotkey="g p" data-analytics-event="{&quot;category&quot;:&quot;Underline navbar&quot;,&quot;action&quot;:&quot;Click tab&quot;,&quot;label&quot;:&quot;Pull requests&quot;,&quot;target&quot;:&quot;UNDERLINE_NAV.TAB&quot;}" data-view-component="true" class="UnderlineNav-item no-wrap js-responsive-underlinenav-item js-selected-navigation-item">
    
              <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-git-pull-request UnderlineNav-octicon d-none d-sm-inline">
    <path d="M1.5 3.25a2.25 2.25 0 1 1 3 2.122v5.256a2.251 2.251 0 1 1-1.5 0V5.372A2.25 2.25 0 0 1 1.5 3.25Zm5.677-.177L9.573.677A.25.25 0 0 1 10 .854V2.5h1A2.5 2.5 0 0 1 13.5 5v5.628a2.251 2.251 0 1 1-1.5 0V5a1 1 0 0 0-1-1h-1v1.646a.25.25 0 0 1-.427.177L7.177 3.427a.25.25 0 0 1 0-.354ZM3.75 2.5a.75.75 0 1 0 0 1.5.75.75 0 0 0 0-1.5Zm0 9.5a.75.75 0 1 0 0 1.5.75.75 0 0 0 0-1.5Zm8.25.75a.75.75 0 1 0 1.5 0 .75.75 0 0 0-1.5 0Z"></path>
</svg>
        <span data-content="Pull requests">Pull requests</span>
          <span id="pull-requests-repo-tab-count" data-pjax-replace="" data-turbo-replace="" title="0" hidden="hidden" data-view-component="true" class="Counter">0</span>


    
</a></li>
      <li data-view-component="true" class="d-inline-flex">
  <a id="actions-tab" href="https://github.com/fastabyq/-Deploy_ke_Streamlit_Cloud/actions" data-tab-item="i3actions-tab" data-selected-links="repo_actions /fastabyq/-Deploy_ke_Streamlit_Cloud/actions" data-pjax="#repo-content-pjax-container" data-turbo-frame="repo-content-turbo-frame" data-hotkey="g a" data-analytics-event="{&quot;category&quot;:&quot;Underline navbar&quot;,&quot;action&quot;:&quot;Click tab&quot;,&quot;label&quot;:&quot;Actions&quot;,&quot;target&quot;:&quot;UNDERLINE_NAV.TAB&quot;}" data-view-component="true" class="UnderlineNav-item no-wrap js-responsive-underlinenav-item js-selected-navigation-item">
    
              <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-play UnderlineNav-octicon d-none d-sm-inline">
    <path d="M8 0a8 8 0 1 1 0 16A8 8 0 0 1 8 0ZM1.5 8a6.5 6.5 0 1 0 13 0 6.5 6.5 0 0 0-13 0Zm4.879-2.773 4.264 2.559a.25.25 0 0 1 0 .428l-4.264 2.559A.25.25 0 0 1 6 10.559V5.442a.25.25 0 0 1 .379-.215Z"></path>
</svg>
        <span data-content="Actions">Actions</span>
          <span id="actions-repo-tab-count" data-pjax-replace="" data-turbo-replace="" title="Not available" data-view-component="true" class="Counter"></span>


    
</a></li>
      <li data-view-component="true" class="d-inline-flex">
  <a id="projects-tab" href="https://github.com/fastabyq/-Deploy_ke_Streamlit_Cloud/projects" data-tab-item="i4projects-tab" data-selected-links="repo_projects new_repo_project repo_project /fastabyq/-Deploy_ke_Streamlit_Cloud/projects" data-pjax="#repo-content-pjax-container" data-turbo-frame="repo-content-turbo-frame" data-hotkey="g b" data-analytics-event="{&quot;category&quot;:&quot;Underline navbar&quot;,&quot;action&quot;:&quot;Click tab&quot;,&quot;label&quot;:&quot;Projects&quot;,&quot;target&quot;:&quot;UNDERLINE_NAV.TAB&quot;}" data-view-component="true" class="UnderlineNav-item no-wrap js-responsive-underlinenav-item js-selected-navigation-item">
    
              <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-table UnderlineNav-octicon d-none d-sm-inline">
    <path d="M0 1.75C0 .784.784 0 1.75 0h12.5C15.216 0 16 .784 16 1.75v12.5A1.75 1.75 0 0 1 14.25 16H1.75A1.75 1.75 0 0 1 0 14.25ZM6.5 6.5v8h7.75a.25.25 0 0 0 .25-.25V6.5Zm8-1.5V1.75a.25.25 0 0 0-.25-.25H6.5V5Zm-13 1.5v7.75c0 .138.112.25.25.25H5v-8ZM5 5V1.5H1.75a.25.25 0 0 0-.25.25V5Z"></path>
</svg>
        <span data-content="Projects">Projects</span>
          <span id="projects-repo-tab-count" data-pjax-replace="" data-turbo-replace="" title="0" hidden="hidden" data-view-component="true" class="Counter">0</span>


    
</a></li>
      <li data-view-component="true" class="d-inline-flex">
  <a id="security-tab" href="https://github.com/fastabyq/-Deploy_ke_Streamlit_Cloud/security" data-tab-item="i5security-tab" data-selected-links="security overview alerts policy token_scanning code_scanning /fastabyq/-Deploy_ke_Streamlit_Cloud/security" data-pjax="#repo-content-pjax-container" data-turbo-frame="repo-content-turbo-frame" data-hotkey="g s" data-analytics-event="{&quot;category&quot;:&quot;Underline navbar&quot;,&quot;action&quot;:&quot;Click tab&quot;,&quot;label&quot;:&quot;Security&quot;,&quot;target&quot;:&quot;UNDERLINE_NAV.TAB&quot;}" data-view-component="true" class="UnderlineNav-item no-wrap js-responsive-underlinenav-item js-selected-navigation-item">
    
              <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-shield UnderlineNav-octicon d-none d-sm-inline">
    <path d="M7.467.133a1.748 1.748 0 0 1 1.066 0l5.25 1.68A1.75 1.75 0 0 1 15 3.48V7c0 1.566-.32 3.182-1.303 4.682-.983 1.498-2.585 2.813-5.032 3.855a1.697 1.697 0 0 1-1.33 0c-2.447-1.042-4.049-2.357-5.032-3.855C1.32 10.182 1 8.566 1 7V3.48a1.75 1.75 0 0 1 1.217-1.667Zm.61 1.429a.25.25 0 0 0-.153 0l-5.25 1.68a.25.25 0 0 0-.174.238V7c0 1.358.275 2.666 1.057 3.86.784 1.194 2.121 2.34 4.366 3.297a.196.196 0 0 0 .154 0c2.245-.956 3.582-2.104 4.366-3.298C13.225 9.666 13.5 8.36 13.5 7V3.48a.251.251 0 0 0-.174-.237l-5.25-1.68ZM8.75 4.75v3a.75.75 0 0 1-1.5 0v-3a.75.75 0 0 1 1.5 0ZM9 10.5a1 1 0 1 1-2 0 1 1 0 0 1 2 0Z"></path>
</svg>
        <span data-content="Security">Security</span>
          </a><div data-show-on-forbidden-error="" hidden=""><a id="security-tab" href="https://github.com/fastabyq/-Deploy_ke_Streamlit_Cloud/security" data-tab-item="i5security-tab" data-selected-links="security overview alerts policy token_scanning code_scanning /fastabyq/-Deploy_ke_Streamlit_Cloud/security" data-pjax="#repo-content-pjax-container" data-turbo-frame="repo-content-turbo-frame" data-hotkey="g s" data-analytics-event="{&quot;category&quot;:&quot;Underline navbar&quot;,&quot;action&quot;:&quot;Click tab&quot;,&quot;label&quot;:&quot;Security&quot;,&quot;target&quot;:&quot;UNDERLINE_NAV.TAB&quot;}" data-view-component="true" class="UnderlineNav-item no-wrap js-responsive-underlinenav-item js-selected-navigation-item">
    </a><div class="Box"><a id="security-tab" href="https://github.com/fastabyq/-Deploy_ke_Streamlit_Cloud/security" data-tab-item="i5security-tab" data-selected-links="security overview alerts policy token_scanning code_scanning /fastabyq/-Deploy_ke_Streamlit_Cloud/security" data-pjax="#repo-content-pjax-container" data-turbo-frame="repo-content-turbo-frame" data-hotkey="g s" data-analytics-event="{&quot;category&quot;:&quot;Underline navbar&quot;,&quot;action&quot;:&quot;Click tab&quot;,&quot;label&quot;:&quot;Security&quot;,&quot;target&quot;:&quot;UNDERLINE_NAV.TAB&quot;}" data-view-component="true" class="UnderlineNav-item no-wrap js-responsive-underlinenav-item js-selected-navigation-item">
  </a><div class="blankslate-container"><a id="security-tab" href="https://github.com/fastabyq/-Deploy_ke_Streamlit_Cloud/security" data-tab-item="i5security-tab" data-selected-links="security overview alerts policy token_scanning code_scanning /fastabyq/-Deploy_ke_Streamlit_Cloud/security" data-pjax="#repo-content-pjax-container" data-turbo-frame="repo-content-turbo-frame" data-hotkey="g s" data-analytics-event="{&quot;category&quot;:&quot;Underline navbar&quot;,&quot;action&quot;:&quot;Click tab&quot;,&quot;label&quot;:&quot;Security&quot;,&quot;target&quot;:&quot;UNDERLINE_NAV.TAB&quot;}" data-view-component="true" class="UnderlineNav-item no-wrap js-responsive-underlinenav-item js-selected-navigation-item">
    </a><div data-view-component="true" class="blankslate blankslate-spacious color-bg-default rounded-2"><a id="security-tab" href="https://github.com/fastabyq/-Deploy_ke_Streamlit_Cloud/security" data-tab-item="i5security-tab" data-selected-links="security overview alerts policy token_scanning code_scanning /fastabyq/-Deploy_ke_Streamlit_Cloud/security" data-pjax="#repo-content-pjax-container" data-turbo-frame="repo-content-turbo-frame" data-hotkey="g s" data-analytics-event="{&quot;category&quot;:&quot;Underline navbar&quot;,&quot;action&quot;:&quot;Click tab&quot;,&quot;label&quot;:&quot;Security&quot;,&quot;target&quot;:&quot;UNDERLINE_NAV.TAB&quot;}" data-view-component="true" class="UnderlineNav-item no-wrap js-responsive-underlinenav-item js-selected-navigation-item">
      

      <h3 data-view-component="true" class="blankslate-heading">        Uh oh!
</h3>
      <p data-view-component="true">        </p></a><p class="color-fg-muted my-2 mb-2 ws-normal"><a id="security-tab" href="https://github.com/fastabyq/-Deploy_ke_Streamlit_Cloud/security" data-tab-item="i5security-tab" data-selected-links="security overview alerts policy token_scanning code_scanning /fastabyq/-Deploy_ke_Streamlit_Cloud/security" data-pjax="#repo-content-pjax-container" data-turbo-frame="repo-content-turbo-frame" data-hotkey="g s" data-analytics-event="{&quot;category&quot;:&quot;Underline navbar&quot;,&quot;action&quot;:&quot;Click tab&quot;,&quot;label&quot;:&quot;Security&quot;,&quot;target&quot;:&quot;UNDERLINE_NAV.TAB&quot;}" data-view-component="true" class="UnderlineNav-item no-wrap js-responsive-underlinenav-item js-selected-navigation-item">There was an error while loading. </a><a class="Link--inTextBlock" data-turbo="false" href="https://github.com/fastabyq/-Deploy_ke_Streamlit_Cloud/blob/main/app.py" aria-label="Please reload this page">Please reload this page</a>.</p>
<p></p>

</div>  </div>
</div>  </div>


    
</li>
      <li data-view-component="true" class="d-inline-flex">
  <a id="insights-tab" href="https://github.com/fastabyq/-Deploy_ke_Streamlit_Cloud/pulse" data-tab-item="i6insights-tab" data-selected-links="repo_graphs repo_contributors dependency_graph dependabot_updates pulse people community /fastabyq/-Deploy_ke_Streamlit_Cloud/pulse" data-pjax="#repo-content-pjax-container" data-turbo-frame="repo-content-turbo-frame" data-analytics-event="{&quot;category&quot;:&quot;Underline navbar&quot;,&quot;action&quot;:&quot;Click tab&quot;,&quot;label&quot;:&quot;Insights&quot;,&quot;target&quot;:&quot;UNDERLINE_NAV.TAB&quot;}" data-view-component="true" class="UnderlineNav-item no-wrap js-responsive-underlinenav-item js-selected-navigation-item">
    
              <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-graph UnderlineNav-octicon d-none d-sm-inline">
    <path d="M1.5 1.75V13.5h13.75a.75.75 0 0 1 0 1.5H.75a.75.75 0 0 1-.75-.75V1.75a.75.75 0 0 1 1.5 0Zm14.28 2.53-5.25 5.25a.75.75 0 0 1-1.06 0L7 7.06 4.28 9.78a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042l3.25-3.25a.75.75 0 0 1 1.06 0L10 7.94l4.72-4.72a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042Z"></path>
</svg>
        <span data-content="Insights">Insights</span>
          <span id="insights-repo-tab-count" data-pjax-replace="" data-turbo-replace="" title="Not available" data-view-component="true" class="Counter"></span>


    
</a></li>
</ul>
    <div style="visibility:hidden;" data-view-component="true" class="UnderlineNav-actions js-responsive-underlinenav-overflow position-absolute pr-3 pr-md-4 pr-lg-5 right-0">      <action-menu data-select-variant="none" data-view-component="true" data-catalyst="" data-ready="true">
  <focus-group direction="vertical" mnemonics="" retain="">
    <button id="action-menu-62409897-dbfd-485c-997f-0dbb5c1dac61-button" popovertarget="action-menu-62409897-dbfd-485c-997f-0dbb5c1dac61-overlay" aria-controls="action-menu-62409897-dbfd-485c-997f-0dbb5c1dac61-list" aria-haspopup="true" aria-labelledby="tooltip-d47b4f02-8390-4546-aadc-975700e9942f" type="button" data-view-component="true" class="Button Button--iconOnly Button--secondary Button--medium UnderlineNav-item">  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-kebab-horizontal Button-visual">
    <path d="M8 9a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3ZM1.5 9a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3Zm13 0a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3Z"></path>
</svg>
</button><tool-tip id="tooltip-d47b4f02-8390-4546-aadc-975700e9942f" for="action-menu-62409897-dbfd-485c-997f-0dbb5c1dac61-button" popover="manual" data-direction="s" data-type="label" data-view-component="true" class="sr-only position-absolute" aria-hidden="true" role="tooltip"><template shadowrootmode="open"><style>
      :host {
        --tooltip-top: var(--tool-tip-position-top, 0);
        --tooltip-left: var(--tool-tip-position-left, 0);
        padding: var(--overlay-paddingBlock-condensed) var(--overlay-padding-condensed) !important;
        font: var(--text-body-shorthand-small);
        color: var(--tooltip-fgColor, var(--fgColor-onEmphasis)) !important;
        text-align: center;
        text-decoration: none;
        text-shadow: none;
        text-transform: none;
        letter-spacing: normal;
        word-wrap: break-word;
        white-space: pre;
        background: var(--tooltip-bgColor, var(--bgColor-emphasis)) !important;
        border-radius: var(--borderRadius-medium);
        border: 0 !important;
        opacity: 0;
        max-width: var(--overlay-width-small);
        word-wrap: break-word;
        white-space: normal;
        width: max-content !important;
        inset: var(--tooltip-top) auto auto var(--tooltip-left) !important;
        overflow: visible !important;
        text-wrap: balance;
      }

      :host(:is(.tooltip-n, .tooltip-nw, .tooltip-ne)) {
        --tooltip-top: calc(var(--tool-tip-position-top, 0) - var(--overlay-offset, 0.25rem));
        --tooltip-left: var(--tool-tip-position-left);
      }

      :host(:is(.tooltip-s, .tooltip-sw, .tooltip-se)) {
        --tooltip-top: calc(var(--tool-tip-position-top, 0) + var(--overlay-offset, 0.25rem));
        --tooltip-left: var(--tool-tip-position-left);
      }

      :host(.tooltip-w) {
        --tooltip-top: var(--tool-tip-position-top);
        --tooltip-left: calc(var(--tool-tip-position-left, 0) - var(--overlay-offset, 0.25rem));
      }

      :host(.tooltip-e) {
        --tooltip-top: var(--tool-tip-position-top);
        --tooltip-left: calc(var(--tool-tip-position-left, 0) + var(--overlay-offset, 0.25rem));
      }

      :host:after{
        position: absolute;
        display: block;
        right: 0;
        left: 0;
        height: var(--overlay-offset, 0.25rem);
        content: "";
      }

      :host(.tooltip-s):after,
      :host(.tooltip-se):after,
      :host(.tooltip-sw):after {
        bottom: 100%
      }

      :host(.tooltip-n):after,
      :host(.tooltip-ne):after,
      :host(.tooltip-nw):after {
        top: 100%;
      }

      @keyframes tooltip-appear {
        from {
          opacity: 0;
        }
        to {
          opacity: 1;
        }
      }

      :host(:popover-open),
      :host(:popover-open):before {
        animation-name: tooltip-appear;
        animation-duration: .1s;
        animation-fill-mode: forwards;
        animation-timing-function: ease-in;
      }

      :host(.\:popover-open) {
        animation-name: tooltip-appear;
        animation-duration: .1s;
        animation-fill-mode: forwards;
        animation-timing-function: ease-in;
      }

      @media (forced-colors: active) {
        :host {
          outline: solid 1px transparent;
        }

        :host:before {
          display: none;
        }
      }
    </style><slot></slot></template>Additional navigation options</tool-tip>


<anchored-position data-target="action-menu.overlay" id="action-menu-62409897-dbfd-485c-997f-0dbb5c1dac61-overlay" anchor="action-menu-62409897-dbfd-485c-997f-0dbb5c1dac61-button" align="start" side="outside-bottom" anchor-offset="normal" popover="auto" data-view-component="true" style="inset: 36px auto auto 0px;">
  <div data-view-component="true" class="Overlay Overlay--size-auto">
    
      <div data-view-component="true" class="Overlay-body Overlay-body--paddingNone">          <action-list data-catalyst="">
  <div data-view-component="true">
    <ul aria-labelledby="action-menu-62409897-dbfd-485c-997f-0dbb5c1dac61-button" id="action-menu-62409897-dbfd-485c-997f-0dbb5c1dac61-list" role="menu" data-view-component="true" class="ActionListWrap--inset ActionListWrap">
        <li hidden="" data-menu-item="i0code-tab" data-targets="action-list.items" role="none" data-view-component="true" class="ActionListItem">
    
    
    <a tabindex="-1" id="item-664d28ae-79a5-4448-a0f0-8372b9cf7df6" href="https://github.com/fastabyq/-Deploy_ke_Streamlit_Cloud" role="menuitem" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-code">
    <path d="m11.28 3.22 4.25 4.25a.75.75 0 0 1 0 1.06l-4.25 4.25a.749.749 0 0 1-1.275-.326.749.749 0 0 1 .215-.734L13.94 8l-3.72-3.72a.749.749 0 0 1 .326-1.275.749.749 0 0 1 .734.215Zm-6.56 0a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042L2.06 8l3.72 3.72a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215L.47 8.53a.75.75 0 0 1 0-1.06Z"></path>
</svg>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
          Code
</span>      
</a>
  
</li>
        <li hidden="" data-menu-item="i1issues-tab" data-targets="action-list.items" role="none" data-view-component="true" class="ActionListItem">
    
    
    <a tabindex="-1" id="item-ef03903e-9793-40cd-b8a5-317dbe2c5ddb" href="https://github.com/fastabyq/-Deploy_ke_Streamlit_Cloud/issues" role="menuitem" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-issue-opened">
    <path d="M8 9.5a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3Z"></path><path d="M8 0a8 8 0 1 1 0 16A8 8 0 0 1 8 0ZM1.5 8a6.5 6.5 0 1 0 13 0 6.5 6.5 0 0 0-13 0Z"></path>
</svg>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
          Issues
</span>      
</a>
  
</li>
        <li hidden="" data-menu-item="i2pull-requests-tab" data-targets="action-list.items" role="none" data-view-component="true" class="ActionListItem">
    
    
    <a tabindex="-1" id="item-07d687cd-6f80-492b-9afe-27e49c110386" href="https://github.com/fastabyq/-Deploy_ke_Streamlit_Cloud/pulls" role="menuitem" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-git-pull-request">
    <path d="M1.5 3.25a2.25 2.25 0 1 1 3 2.122v5.256a2.251 2.251 0 1 1-1.5 0V5.372A2.25 2.25 0 0 1 1.5 3.25Zm5.677-.177L9.573.677A.25.25 0 0 1 10 .854V2.5h1A2.5 2.5 0 0 1 13.5 5v5.628a2.251 2.251 0 1 1-1.5 0V5a1 1 0 0 0-1-1h-1v1.646a.25.25 0 0 1-.427.177L7.177 3.427a.25.25 0 0 1 0-.354ZM3.75 2.5a.75.75 0 1 0 0 1.5.75.75 0 0 0 0-1.5Zm0 9.5a.75.75 0 1 0 0 1.5.75.75 0 0 0 0-1.5Zm8.25.75a.75.75 0 1 0 1.5 0 .75.75 0 0 0-1.5 0Z"></path>
</svg>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
          Pull requests
</span>      
</a>
  
</li>
        <li hidden="" data-menu-item="i3actions-tab" data-targets="action-list.items" role="none" data-view-component="true" class="ActionListItem">
    
    
    <a tabindex="-1" id="item-dc1f840c-468f-4419-b49e-a882ad916422" href="https://github.com/fastabyq/-Deploy_ke_Streamlit_Cloud/actions" role="menuitem" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-play">
    <path d="M8 0a8 8 0 1 1 0 16A8 8 0 0 1 8 0ZM1.5 8a6.5 6.5 0 1 0 13 0 6.5 6.5 0 0 0-13 0Zm4.879-2.773 4.264 2.559a.25.25 0 0 1 0 .428l-4.264 2.559A.25.25 0 0 1 6 10.559V5.442a.25.25 0 0 1 .379-.215Z"></path>
</svg>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
          Actions
</span>      
</a>
  
</li>
        <li hidden="" data-menu-item="i4projects-tab" data-targets="action-list.items" role="none" data-view-component="true" class="ActionListItem">
    
    
    <a tabindex="-1" id="item-3bdceada-b4c3-4023-b3b2-34de365dcf5b" href="https://github.com/fastabyq/-Deploy_ke_Streamlit_Cloud/projects" role="menuitem" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-table">
    <path d="M0 1.75C0 .784.784 0 1.75 0h12.5C15.216 0 16 .784 16 1.75v12.5A1.75 1.75 0 0 1 14.25 16H1.75A1.75 1.75 0 0 1 0 14.25ZM6.5 6.5v8h7.75a.25.25 0 0 0 .25-.25V6.5Zm8-1.5V1.75a.25.25 0 0 0-.25-.25H6.5V5Zm-13 1.5v7.75c0 .138.112.25.25.25H5v-8ZM5 5V1.5H1.75a.25.25 0 0 0-.25.25V5Z"></path>
</svg>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
          Projects
</span>      
</a>
  
</li>
        <li hidden="" data-menu-item="i5security-tab" data-targets="action-list.items" role="none" data-view-component="true" class="ActionListItem">
    
    
    <a tabindex="-1" id="item-8b1ffc8f-4e0d-4cd6-b9bd-8db433abac24" href="https://github.com/fastabyq/-Deploy_ke_Streamlit_Cloud/security" role="menuitem" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-shield">
    <path d="M7.467.133a1.748 1.748 0 0 1 1.066 0l5.25 1.68A1.75 1.75 0 0 1 15 3.48V7c0 1.566-.32 3.182-1.303 4.682-.983 1.498-2.585 2.813-5.032 3.855a1.697 1.697 0 0 1-1.33 0c-2.447-1.042-4.049-2.357-5.032-3.855C1.32 10.182 1 8.566 1 7V3.48a1.75 1.75 0 0 1 1.217-1.667Zm.61 1.429a.25.25 0 0 0-.153 0l-5.25 1.68a.25.25 0 0 0-.174.238V7c0 1.358.275 2.666 1.057 3.86.784 1.194 2.121 2.34 4.366 3.297a.196.196 0 0 0 .154 0c2.245-.956 3.582-2.104 4.366-3.298C13.225 9.666 13.5 8.36 13.5 7V3.48a.251.251 0 0 0-.174-.237l-5.25-1.68ZM8.75 4.75v3a.75.75 0 0 1-1.5 0v-3a.75.75 0 0 1 1.5 0ZM9 10.5a1 1 0 1 1-2 0 1 1 0 0 1 2 0Z"></path>
</svg>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
          Security
</span>      
</a>
  
</li>
        <li hidden="" data-menu-item="i6insights-tab" data-targets="action-list.items" role="none" data-view-component="true" class="ActionListItem">
    
    
    <a tabindex="-1" id="item-20f56293-1b47-44ae-bd5b-a61cc967504c" href="https://github.com/fastabyq/-Deploy_ke_Streamlit_Cloud/pulse" role="menuitem" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-graph">
    <path d="M1.5 1.75V13.5h13.75a.75.75 0 0 1 0 1.5H.75a.75.75 0 0 1-.75-.75V1.75a.75.75 0 0 1 1.5 0Zm14.28 2.53-5.25 5.25a.75.75 0 0 1-1.06 0L7 7.06 4.28 9.78a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042l3.25-3.25a.75.75 0 0 1 1.06 0L10 7.94l4.72-4.72a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042Z"></path>
</svg>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
          Insights
</span>      
</a>
  
</li>
</ul>    
</div></action-list>


</div>
      
</div></anchored-position>  </focus-group>
</action-menu></div>
</nav>
          
        </div>
</header>


      <div hidden="hidden" data-view-component="true" class="js-stale-session-flash stale-session-flash flash flash-warn flash-full">
  
        <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-alert">
    <path d="M6.457 1.047c.659-1.234 2.427-1.234 3.086 0l6.082 11.378A1.75 1.75 0 0 1 14.082 15H1.918a1.75 1.75 0 0 1-1.543-2.575Zm1.763.707a.25.25 0 0 0-.44 0L1.698 13.132a.25.25 0 0 0 .22.368h12.164a.25.25 0 0 0 .22-.368Zm.53 3.996v2.5a.75.75 0 0 1-1.5 0v-2.5a.75.75 0 0 1 1.5 0ZM9 11a1 1 0 1 1-2 0 1 1 0 0 1 2 0Z"></path>
</svg>
        <span class="js-stale-session-flash-signed-in" hidden="">You signed in with another tab or window. <a class="Link--inTextBlock" href="https://github.com/fastabyq/-Deploy_ke_Streamlit_Cloud/blob/main/app.py">Reload</a> to refresh your session.</span>
        <span class="js-stale-session-flash-signed-out" hidden="">You signed out in another tab or window. <a class="Link--inTextBlock" href="https://github.com/fastabyq/-Deploy_ke_Streamlit_Cloud/blob/main/app.py">Reload</a> to refresh your session.</span>
        <span class="js-stale-session-flash-switched" hidden="">You switched accounts on another tab or window. <a class="Link--inTextBlock" href="https://github.com/fastabyq/-Deploy_ke_Streamlit_Cloud/blob/main/app.py">Reload</a> to refresh your session.</span>

    <button id="icon-button-f1249eab-2b24-4e46-9469-3d2525115ae3" aria-labelledby="tooltip-1930b6da-9a73-4688-9c62-98c9b13ab6f0" type="button" data-view-component="true" class="Button Button--iconOnly Button--invisible Button--medium flash-close js-flash-close">  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-x Button-visual">
    <path d="M3.72 3.72a.75.75 0 0 1 1.06 0L8 6.94l3.22-3.22a.749.749 0 0 1 1.275.326.749.749 0 0 1-.215.734L9.06 8l3.22 3.22a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215L8 9.06l-3.22 3.22a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042L6.94 8 3.72 4.78a.75.75 0 0 1 0-1.06Z"></path>
</svg>
</button><tool-tip id="tooltip-1930b6da-9a73-4688-9c62-98c9b13ab6f0" for="icon-button-f1249eab-2b24-4e46-9469-3d2525115ae3" popover="manual" data-direction="s" data-type="label" data-view-component="true" class="sr-only position-absolute" aria-hidden="true" role="tooltip"><template shadowrootmode="open"><style>
      :host {
        --tooltip-top: var(--tool-tip-position-top, 0);
        --tooltip-left: var(--tool-tip-position-left, 0);
        padding: var(--overlay-paddingBlock-condensed) var(--overlay-padding-condensed) !important;
        font: var(--text-body-shorthand-small);
        color: var(--tooltip-fgColor, var(--fgColor-onEmphasis)) !important;
        text-align: center;
        text-decoration: none;
        text-shadow: none;
        text-transform: none;
        letter-spacing: normal;
        word-wrap: break-word;
        white-space: pre;
        background: var(--tooltip-bgColor, var(--bgColor-emphasis)) !important;
        border-radius: var(--borderRadius-medium);
        border: 0 !important;
        opacity: 0;
        max-width: var(--overlay-width-small);
        word-wrap: break-word;
        white-space: normal;
        width: max-content !important;
        inset: var(--tooltip-top) auto auto var(--tooltip-left) !important;
        overflow: visible !important;
        text-wrap: balance;
      }

      :host(:is(.tooltip-n, .tooltip-nw, .tooltip-ne)) {
        --tooltip-top: calc(var(--tool-tip-position-top, 0) - var(--overlay-offset, 0.25rem));
        --tooltip-left: var(--tool-tip-position-left);
      }

      :host(:is(.tooltip-s, .tooltip-sw, .tooltip-se)) {
        --tooltip-top: calc(var(--tool-tip-position-top, 0) + var(--overlay-offset, 0.25rem));
        --tooltip-left: var(--tool-tip-position-left);
      }

      :host(.tooltip-w) {
        --tooltip-top: var(--tool-tip-position-top);
        --tooltip-left: calc(var(--tool-tip-position-left, 0) - var(--overlay-offset, 0.25rem));
      }

      :host(.tooltip-e) {
        --tooltip-top: var(--tool-tip-position-top);
        --tooltip-left: calc(var(--tool-tip-position-left, 0) + var(--overlay-offset, 0.25rem));
      }

      :host:after{
        position: absolute;
        display: block;
        right: 0;
        left: 0;
        height: var(--overlay-offset, 0.25rem);
        content: "";
      }

      :host(.tooltip-s):after,
      :host(.tooltip-se):after,
      :host(.tooltip-sw):after {
        bottom: 100%
      }

      :host(.tooltip-n):after,
      :host(.tooltip-ne):after,
      :host(.tooltip-nw):after {
        top: 100%;
      }

      @keyframes tooltip-appear {
        from {
          opacity: 0;
        }
        to {
          opacity: 1;
        }
      }

      :host(:popover-open),
      :host(:popover-open):before {
        animation-name: tooltip-appear;
        animation-duration: .1s;
        animation-fill-mode: forwards;
        animation-timing-function: ease-in;
      }

      :host(.\:popover-open) {
        animation-name: tooltip-appear;
        animation-duration: .1s;
        animation-fill-mode: forwards;
        animation-timing-function: ease-in;
      }

      @media (forced-colors: active) {
        :host {
          outline: solid 1px transparent;
        }

        :host:before {
          display: none;
        }
      }
    </style><slot></slot></template>Dismiss alert</tool-tip>


  
</div>
          
    </div>

  <div id="start-of-content" class="show-on-focus"></div>








    <div id="js-flash-container" class="flash-container" data-turbo-replace="">




  <template class="js-flash-template"></template>
</div>


    
  <notification-shelf-watcher data-base-url="https://github.com/notifications/beta/shelf" data-channel="eyJjIjoibm90aWZpY2F0aW9uLWNoYW5nZWQ6MTI4MTMwMzQ3IiwidCI6MTc1MDA2Mjg0N30=--c6e3ea4ddf03c8b6f396e3e81b0291b4a0579d7c57f1bd444a725f44337f7b3c" data-view-component="true" class="js-socket-channel" data-refresh-delay="500" data-catalyst="" data-throttle-delay="5000"></notification-shelf-watcher>
  <div hidden="" data-initial="" data-target="notification-shelf-watcher.placeholder"></div>






  <div class="application-main " data-commit-hovercards-enabled="" data-discussion-hovercards-enabled="" data-issue-and-pr-hovercards-enabled="" data-project-hovercards-enabled="">
        <div itemscope="" itemtype="http://schema.org/SoftwareSourceCode" class="">
    <main id="js-repo-pjax-container">
      
      






    
  <div id="repository-container-header" data-turbo-replace="" hidden=""></div>




<turbo-frame id="repo-content-turbo-frame" target="_top" data-turbo-action="advance" class="">
    <div id="repo-content-pjax-container" class="repository-content ">
      <a href="https://github.dev/" class="d-none js-github-dev-shortcut" data-hotkey=".,Mod+Alt+.">Open in github.dev</a>
  <a href="https://github.dev/" class="d-none js-github-dev-new-tab-shortcut" data-hotkey="Shift+.,Shift+&gt;,&gt;" target="_blank" rel="noopener noreferrer">Open in a new github.dev tab</a>
    <a class="d-none" data-hotkey=",,Mod+Alt+," target="_blank" href="https://github.com/codespaces/new/fastabyq/-Deploy_ke_Streamlit_Cloud/tree/main?resume=1">Open in codespace</a>




    
      
    








<react-app app-name="react-code-view" initial-path="/fastabyq/-Deploy_ke_Streamlit_Cloud/blob/main/app.py" style="display: block; min-height: calc(100vh - 64px);" data-attempted-ssr="true" data-ssr="true" data-lazy="false" data-alternate="false" data-data-router-enabled="false" data-react-profiling="false" data-catalyst="" class="loaded">
  
  <script type="application/json" data-target="react-app.embeddedData">{"payload":{"allShortcutsEnabled":true,"fileTree":{"":{"items":[{"name":"README.md","path":"README.md","contentType":"file"},{"name":"app.py","path":"app.py","contentType":"file"},{"name":"model_obesitas.pkl","path":"model_obesitas.pkl","contentType":"file"},{"name":"requirements.txt","path":"requirements.txt","contentType":"file"},{"name":"scaler.pkl","path":"scaler.pkl","contentType":"file"}],"totalCount":5}},"fileTreeProcessingTime":1.569153,"foldersToFetch":[],"incompleteFileTree":false,"repo":{"id":994512716,"defaultBranch":"main","name":"-Deploy_ke_Streamlit_Cloud","ownerLogin":"fastabyq","currentUserCanPush":false,"isFork":false,"isEmpty":false,"createdAt":"2025-06-01T20:56:34.000-07:00","ownerAvatar":"https://avatars.githubusercontent.com/u/171785532?v=4","public":true,"private":false,"isOrgOwned":false},"codeLineWrapEnabled":false,"symbolsExpanded":false,"treeExpanded":true,"refInfo":{"name":"main","listCacheKey":"v0:1748836594.0","canEdit":true,"refType":"branch","currentOid":"da85b358297298a9cb40e00378ca9ef5d17989f3"},"path":"app.py","currentUser":{"id":128130347,"login":"Jetgar","userEmail":"111202214316@mhs.dinus.ac.id"},"blob":{"rawLines":["import streamlit as st\r","import numpy as np\r","import joblib\r","\r","# Load model dan scaler\r","model = joblib.load(\"model_obesitas.pkl\")\r","scaler = joblib.load(\"scaler.pkl\")\r","\r","# Judul Aplikasi\r","st.title(\"Prediksi Tingkat Obesitas\")\r","st.markdown(\"Masukkan data berikut untuk memprediksi tingkat obesitas:\")\r","\r","# Input data\r","age = st.number_input(\"Usia\", 10, 100, 25)\r","height = st.number_input(\"Tinggi Badan (meter)\", 1.0, 2.5, 1.70)\r","weight = st.number_input(\"Berat Badan (kg)\", 30, 200, 70)\r","fcvc = st.slider(\"Konsumsi Sayur (FCVC)\", 1, 3, 2)\r","ncp = st.slider(\"Jumlah Makan per Hari (NCP)\", 1, 4, 3)\r","ch2o = st.slider(\"Minum Air (CH2O)\", 1, 3, 2)\r","faf = st.slider(\"Aktivitas Fisik (FAF)\", 0, 3, 1)\r","tue = st.slider(\"Waktu Pakai Teknologi (TUE)\", 0, 3, 1)\r","\r","# Fitur kategorikal\r","gender = st.selectbox(\"Jenis Kelamin\", [\"Male\", \"Female\"])\r","family_history = st.selectbox(\"Riwayat Keluarga Obesitas\", [\"Yes\", \"No\"])\r","favc = st.selectbox(\"Sering Konsumsi Makanan Tinggi Kalori?\", [\"Yes\", \"No\"])\r","caec = st.selectbox(\"Konsumsi Camilan?\", [\"No\", \"Sometimes\", \"Frequently\", \"Always\"])\r","smoke = st.selectbox(\"Merokok?\", [\"Yes\", \"No\"])\r","scc = st.selectbox(\"Kendalikan Kalori?\", [\"Yes\", \"No\"])\r","calc = st.selectbox(\"Konsumsi Alkohol?\", [\"No\", \"Sometimes\", \"Frequently\"])\r","mtrans = st.selectbox(\"Transportasi\", [\"Public_Transportation\", \"Walking\", \"Automobile\", \"Motorbike\", \"Bike\"])\r","\r","# Encode kategorikal manual (harus sama dengan label encoder kamu saat training)\r","def encode(val, mapping):\r","    return mapping.get(val, 0)\r","\r","gender_map = {\"Male\": 1, \"Female\": 0}\r","family_map = {\"Yes\": 1, \"No\": 0}\r","favc_map = {\"Yes\": 1, \"No\": 0}\r","caec_map = {\"No\": 0, \"Sometimes\": 1, \"Frequently\": 2, \"Always\": 3}\r","smoke_map = {\"Yes\": 1, \"No\": 0}\r","scc_map = {\"Yes\": 1, \"No\": 0}\r","calc_map = {\"No\": 0, \"Sometimes\": 1, \"Frequently\": 2}\r","mtrans_map = {\"Public_Transportation\": 0, \"Walking\": 1, \"Automobile\": 2, \"Motorbike\": 3, \"Bike\": 4}\r","\r","# Gabungkan input\r","data = np.array([[\r","    age,\r","    height,\r","    weight,\r","    fcvc,\r","    ncp,\r","    ch2o,\r","    faf,\r","    tue,\r","    encode(gender, gender_map),\r","    encode(family_history, family_map),\r","    encode(favc, favc_map),\r","    encode(caec, caec_map),\r","    encode(smoke, smoke_map),\r","    encode(scc, scc_map),\r","    encode(calc, calc_map),\r","    encode(mtrans, mtrans_map)\r","]])\r","\r","# Tombol prediksi\r","if st.button(\"Prediksi\"):\r","    data_scaled = scaler.transform(data)\r","    pred = model.predict(data_scaled)[0]\r","    \r","    klasifikasi = {\r","        0: \"Berat Badan Kurang\",\r","        1: \"Berat Badan Normal\",\r","        2: \"Kelebihan Berat Badan Tingkat I\",\r","        3: \"Kelebihan Berat Badan Tingkat II\",\r","        4: \"Obesitas Tipe I\",\r","        5: \"Obesitas Tipe II\",\r","        6: \"Obesitas Tipe III\"\r","    }\r","    st.success(f\"Hasil Prediksi: **{klasifikasi[pred]}**\")\r"],"stylingDirectives":null,"colorizedLines":["\u003cspan class=pl-k\u003eimport\u003c/span\u003e \u003cspan class=pl-s1\u003estreamlit\u003c/span\u003e \u003cspan class=pl-k\u003eas\u003c/span\u003e \u003cspan class=pl-s1\u003est\u003c/span\u003e","\u003cspan class=pl-k\u003eimport\u003c/span\u003e \u003cspan class=pl-s1\u003enumpy\u003c/span\u003e \u003cspan class=pl-k\u003eas\u003c/span\u003e \u003cspan class=pl-s1\u003enp\u003c/span\u003e","\u003cspan class=pl-k\u003eimport\u003c/span\u003e \u003cspan class=pl-s1\u003ejoblib\u003c/span\u003e","","\u003cspan class=pl-c\u003e# Load model dan scaler\u003c/span\u003e","\u003cspan class=pl-s1\u003emodel\u003c/span\u003e \u003cspan class=pl-c1\u003e=\u003c/span\u003e \u003cspan class=pl-s1\u003ejoblib\u003c/span\u003e.\u003cspan class=pl-c1\u003eload\u003c/span\u003e(\u003cspan class=pl-s\u003e\u0026quot;model_obesitas.pkl\u0026quot;\u003c/span\u003e)","\u003cspan class=pl-s1\u003escaler\u003c/span\u003e \u003cspan class=pl-c1\u003e=\u003c/span\u003e \u003cspan class=pl-s1\u003ejoblib\u003c/span\u003e.\u003cspan class=pl-c1\u003eload\u003c/span\u003e(\u003cspan class=pl-s\u003e\u0026quot;scaler.pkl\u0026quot;\u003c/span\u003e)","","\u003cspan class=pl-c\u003e# Judul Aplikasi\u003c/span\u003e","\u003cspan class=pl-s1\u003est\u003c/span\u003e.\u003cspan class=pl-c1\u003etitle\u003c/span\u003e(\u003cspan class=pl-s\u003e\u0026quot;Prediksi Tingkat Obesitas\u0026quot;\u003c/span\u003e)","\u003cspan class=pl-s1\u003est\u003c/span\u003e.\u003cspan class=pl-c1\u003emarkdown\u003c/span\u003e(\u003cspan class=pl-s\u003e\u0026quot;Masukkan data berikut untuk memprediksi tingkat obesitas:\u0026quot;\u003c/span\u003e)","","\u003cspan class=pl-c\u003e# Input data\u003c/span\u003e","\u003cspan class=pl-s1\u003eage\u003c/span\u003e \u003cspan class=pl-c1\u003e=\u003c/span\u003e \u003cspan class=pl-s1\u003est\u003c/span\u003e.\u003cspan class=pl-c1\u003enumber_input\u003c/span\u003e(\u003cspan class=pl-s\u003e\u0026quot;Usia\u0026quot;\u003c/span\u003e, \u003cspan class=pl-c1\u003e10\u003c/span\u003e, \u003cspan class=pl-c1\u003e100\u003c/span\u003e, \u003cspan class=pl-c1\u003e25\u003c/span\u003e)","\u003cspan class=pl-s1\u003eheight\u003c/span\u003e \u003cspan class=pl-c1\u003e=\u003c/span\u003e \u003cspan class=pl-s1\u003est\u003c/span\u003e.\u003cspan class=pl-c1\u003enumber_input\u003c/span\u003e(\u003cspan class=pl-s\u003e\u0026quot;Tinggi Badan (meter)\u0026quot;\u003c/span\u003e, \u003cspan class=pl-c1\u003e1.0\u003c/span\u003e, \u003cspan class=pl-c1\u003e2.5\u003c/span\u003e, \u003cspan class=pl-c1\u003e1.70\u003c/span\u003e)","\u003cspan class=pl-s1\u003eweight\u003c/span\u003e \u003cspan class=pl-c1\u003e=\u003c/span\u003e \u003cspan class=pl-s1\u003est\u003c/span\u003e.\u003cspan class=pl-c1\u003enumber_input\u003c/span\u003e(\u003cspan class=pl-s\u003e\u0026quot;Berat Badan (kg)\u0026quot;\u003c/span\u003e, \u003cspan class=pl-c1\u003e30\u003c/span\u003e, \u003cspan class=pl-c1\u003e200\u003c/span\u003e, \u003cspan class=pl-c1\u003e70\u003c/span\u003e)","\u003cspan class=pl-s1\u003efcvc\u003c/span\u003e \u003cspan class=pl-c1\u003e=\u003c/span\u003e \u003cspan class=pl-s1\u003est\u003c/span\u003e.\u003cspan class=pl-c1\u003eslider\u003c/span\u003e(\u003cspan class=pl-s\u003e\u0026quot;Konsumsi Sayur (FCVC)\u0026quot;\u003c/span\u003e, \u003cspan class=pl-c1\u003e1\u003c/span\u003e, \u003cspan class=pl-c1\u003e3\u003c/span\u003e, \u003cspan class=pl-c1\u003e2\u003c/span\u003e)","\u003cspan class=pl-s1\u003encp\u003c/span\u003e \u003cspan class=pl-c1\u003e=\u003c/span\u003e \u003cspan class=pl-s1\u003est\u003c/span\u003e.\u003cspan class=pl-c1\u003eslider\u003c/span\u003e(\u003cspan class=pl-s\u003e\u0026quot;Jumlah Makan per Hari (NCP)\u0026quot;\u003c/span\u003e, \u003cspan class=pl-c1\u003e1\u003c/span\u003e, \u003cspan class=pl-c1\u003e4\u003c/span\u003e, \u003cspan class=pl-c1\u003e3\u003c/span\u003e)","\u003cspan class=pl-s1\u003ech2o\u003c/span\u003e \u003cspan class=pl-c1\u003e=\u003c/span\u003e \u003cspan class=pl-s1\u003est\u003c/span\u003e.\u003cspan class=pl-c1\u003eslider\u003c/span\u003e(\u003cspan class=pl-s\u003e\u0026quot;Minum Air (CH2O)\u0026quot;\u003c/span\u003e, \u003cspan class=pl-c1\u003e1\u003c/span\u003e, \u003cspan class=pl-c1\u003e3\u003c/span\u003e, \u003cspan class=pl-c1\u003e2\u003c/span\u003e)","\u003cspan class=pl-s1\u003efaf\u003c/span\u003e \u003cspan class=pl-c1\u003e=\u003c/span\u003e \u003cspan class=pl-s1\u003est\u003c/span\u003e.\u003cspan class=pl-c1\u003eslider\u003c/span\u003e(\u003cspan class=pl-s\u003e\u0026quot;Aktivitas Fisik (FAF)\u0026quot;\u003c/span\u003e, \u003cspan class=pl-c1\u003e0\u003c/span\u003e, \u003cspan class=pl-c1\u003e3\u003c/span\u003e, \u003cspan class=pl-c1\u003e1\u003c/span\u003e)","\u003cspan class=pl-s1\u003etue\u003c/span\u003e \u003cspan class=pl-c1\u003e=\u003c/span\u003e \u003cspan class=pl-s1\u003est\u003c/span\u003e.\u003cspan class=pl-c1\u003eslider\u003c/span\u003e(\u003cspan class=pl-s\u003e\u0026quot;Waktu Pakai Teknologi (TUE)\u0026quot;\u003c/span\u003e, \u003cspan class=pl-c1\u003e0\u003c/span\u003e, \u003cspan class=pl-c1\u003e3\u003c/span\u003e, \u003cspan class=pl-c1\u003e1\u003c/span\u003e)","","\u003cspan class=pl-c\u003e# Fitur kategorikal\u003c/span\u003e","\u003cspan class=pl-s1\u003egender\u003c/span\u003e \u003cspan class=pl-c1\u003e=\u003c/span\u003e \u003cspan class=pl-s1\u003est\u003c/span\u003e.\u003cspan class=pl-c1\u003eselectbox\u003c/span\u003e(\u003cspan class=pl-s\u003e\u0026quot;Jenis Kelamin\u0026quot;\u003c/span\u003e, [\u003cspan class=pl-s\u003e\u0026quot;Male\u0026quot;\u003c/span\u003e, \u003cspan class=pl-s\u003e\u0026quot;Female\u0026quot;\u003c/span\u003e])","\u003cspan class=pl-s1\u003efamily_history\u003c/span\u003e \u003cspan class=pl-c1\u003e=\u003c/span\u003e \u003cspan class=pl-s1\u003est\u003c/span\u003e.\u003cspan class=pl-c1\u003eselectbox\u003c/span\u003e(\u003cspan class=pl-s\u003e\u0026quot;Riwayat Keluarga Obesitas\u0026quot;\u003c/span\u003e, [\u003cspan class=pl-s\u003e\u0026quot;Yes\u0026quot;\u003c/span\u003e, \u003cspan class=pl-s\u003e\u0026quot;No\u0026quot;\u003c/span\u003e])","\u003cspan class=pl-s1\u003efavc\u003c/span\u003e \u003cspan class=pl-c1\u003e=\u003c/span\u003e \u003cspan class=pl-s1\u003est\u003c/span\u003e.\u003cspan class=pl-c1\u003eselectbox\u003c/span\u003e(\u003cspan class=pl-s\u003e\u0026quot;Sering Konsumsi Makanan Tinggi Kalori?\u0026quot;\u003c/span\u003e, [\u003cspan class=pl-s\u003e\u0026quot;Yes\u0026quot;\u003c/span\u003e, \u003cspan class=pl-s\u003e\u0026quot;No\u0026quot;\u003c/span\u003e])","\u003cspan class=pl-s1\u003ecaec\u003c/span\u003e \u003cspan class=pl-c1\u003e=\u003c/span\u003e \u003cspan class=pl-s1\u003est\u003c/span\u003e.\u003cspan class=pl-c1\u003eselectbox\u003c/span\u003e(\u003cspan class=pl-s\u003e\u0026quot;Konsumsi Camilan?\u0026quot;\u003c/span\u003e, [\u003cspan class=pl-s\u003e\u0026quot;No\u0026quot;\u003c/span\u003e, \u003cspan class=pl-s\u003e\u0026quot;Sometimes\u0026quot;\u003c/span\u003e, \u003cspan class=pl-s\u003e\u0026quot;Frequently\u0026quot;\u003c/span\u003e, \u003cspan class=pl-s\u003e\u0026quot;Always\u0026quot;\u003c/span\u003e])","\u003cspan class=pl-s1\u003esmoke\u003c/span\u003e \u003cspan class=pl-c1\u003e=\u003c/span\u003e \u003cspan class=pl-s1\u003est\u003c/span\u003e.\u003cspan class=pl-c1\u003eselectbox\u003c/span\u003e(\u003cspan class=pl-s\u003e\u0026quot;Merokok?\u0026quot;\u003c/span\u003e, [\u003cspan class=pl-s\u003e\u0026quot;Yes\u0026quot;\u003c/span\u003e, \u003cspan class=pl-s\u003e\u0026quot;No\u0026quot;\u003c/span\u003e])","\u003cspan class=pl-s1\u003escc\u003c/span\u003e \u003cspan class=pl-c1\u003e=\u003c/span\u003e \u003cspan class=pl-s1\u003est\u003c/span\u003e.\u003cspan class=pl-c1\u003eselectbox\u003c/span\u003e(\u003cspan class=pl-s\u003e\u0026quot;Kendalikan Kalori?\u0026quot;\u003c/span\u003e, [\u003cspan class=pl-s\u003e\u0026quot;Yes\u0026quot;\u003c/span\u003e, \u003cspan class=pl-s\u003e\u0026quot;No\u0026quot;\u003c/span\u003e])","\u003cspan class=pl-s1\u003ecalc\u003c/span\u003e \u003cspan class=pl-c1\u003e=\u003c/span\u003e \u003cspan class=pl-s1\u003est\u003c/span\u003e.\u003cspan class=pl-c1\u003eselectbox\u003c/span\u003e(\u003cspan class=pl-s\u003e\u0026quot;Konsumsi Alkohol?\u0026quot;\u003c/span\u003e, [\u003cspan class=pl-s\u003e\u0026quot;No\u0026quot;\u003c/span\u003e, \u003cspan class=pl-s\u003e\u0026quot;Sometimes\u0026quot;\u003c/span\u003e, \u003cspan class=pl-s\u003e\u0026quot;Frequently\u0026quot;\u003c/span\u003e])","\u003cspan class=pl-s1\u003emtrans\u003c/span\u003e \u003cspan class=pl-c1\u003e=\u003c/span\u003e \u003cspan class=pl-s1\u003est\u003c/span\u003e.\u003cspan class=pl-c1\u003eselectbox\u003c/span\u003e(\u003cspan class=pl-s\u003e\u0026quot;Transportasi\u0026quot;\u003c/span\u003e, [\u003cspan class=pl-s\u003e\u0026quot;Public_Transportation\u0026quot;\u003c/span\u003e, \u003cspan class=pl-s\u003e\u0026quot;Walking\u0026quot;\u003c/span\u003e, \u003cspan class=pl-s\u003e\u0026quot;Automobile\u0026quot;\u003c/span\u003e, \u003cspan class=pl-s\u003e\u0026quot;Motorbike\u0026quot;\u003c/span\u003e, \u003cspan class=pl-s\u003e\u0026quot;Bike\u0026quot;\u003c/span\u003e])","","\u003cspan class=pl-c\u003e# Encode kategorikal manual (harus sama dengan label encoder kamu saat training)\u003c/span\u003e","\u003cspan class=pl-k\u003edef\u003c/span\u003e \u003cspan class=pl-en\u003eencode\u003c/span\u003e(\u003cspan class=pl-s1\u003eval\u003c/span\u003e, \u003cspan class=pl-s1\u003emapping\u003c/span\u003e):","    \u003cspan class=pl-k\u003ereturn\u003c/span\u003e \u003cspan class=pl-s1\u003emapping\u003c/span\u003e.\u003cspan class=pl-c1\u003eget\u003c/span\u003e(\u003cspan class=pl-s1\u003eval\u003c/span\u003e, \u003cspan class=pl-c1\u003e0\u003c/span\u003e)","","\u003cspan class=pl-s1\u003egender_map\u003c/span\u003e \u003cspan class=pl-c1\u003e=\u003c/span\u003e {\u003cspan class=pl-s\u003e\u0026quot;Male\u0026quot;\u003c/span\u003e: \u003cspan class=pl-c1\u003e1\u003c/span\u003e, \u003cspan class=pl-s\u003e\u0026quot;Female\u0026quot;\u003c/span\u003e: \u003cspan class=pl-c1\u003e0\u003c/span\u003e}","\u003cspan class=pl-s1\u003efamily_map\u003c/span\u003e \u003cspan class=pl-c1\u003e=\u003c/span\u003e {\u003cspan class=pl-s\u003e\u0026quot;Yes\u0026quot;\u003c/span\u003e: \u003cspan class=pl-c1\u003e1\u003c/span\u003e, \u003cspan class=pl-s\u003e\u0026quot;No\u0026quot;\u003c/span\u003e: \u003cspan class=pl-c1\u003e0\u003c/span\u003e}","\u003cspan class=pl-s1\u003efavc_map\u003c/span\u003e \u003cspan class=pl-c1\u003e=\u003c/span\u003e {\u003cspan class=pl-s\u003e\u0026quot;Yes\u0026quot;\u003c/span\u003e: \u003cspan class=pl-c1\u003e1\u003c/span\u003e, \u003cspan class=pl-s\u003e\u0026quot;No\u0026quot;\u003c/span\u003e: \u003cspan class=pl-c1\u003e0\u003c/span\u003e}","\u003cspan class=pl-s1\u003ecaec_map\u003c/span\u003e \u003cspan class=pl-c1\u003e=\u003c/span\u003e {\u003cspan class=pl-s\u003e\u0026quot;No\u0026quot;\u003c/span\u003e: \u003cspan class=pl-c1\u003e0\u003c/span\u003e, \u003cspan class=pl-s\u003e\u0026quot;Sometimes\u0026quot;\u003c/span\u003e: \u003cspan class=pl-c1\u003e1\u003c/span\u003e, \u003cspan class=pl-s\u003e\u0026quot;Frequently\u0026quot;\u003c/span\u003e: \u003cspan class=pl-c1\u003e2\u003c/span\u003e, \u003cspan class=pl-s\u003e\u0026quot;Always\u0026quot;\u003c/span\u003e: \u003cspan class=pl-c1\u003e3\u003c/span\u003e}","\u003cspan class=pl-s1\u003esmoke_map\u003c/span\u003e \u003cspan class=pl-c1\u003e=\u003c/span\u003e {\u003cspan class=pl-s\u003e\u0026quot;Yes\u0026quot;\u003c/span\u003e: \u003cspan class=pl-c1\u003e1\u003c/span\u003e, \u003cspan class=pl-s\u003e\u0026quot;No\u0026quot;\u003c/span\u003e: \u003cspan class=pl-c1\u003e0\u003c/span\u003e}","\u003cspan class=pl-s1\u003escc_map\u003c/span\u003e \u003cspan class=pl-c1\u003e=\u003c/span\u003e {\u003cspan class=pl-s\u003e\u0026quot;Yes\u0026quot;\u003c/span\u003e: \u003cspan class=pl-c1\u003e1\u003c/span\u003e, \u003cspan class=pl-s\u003e\u0026quot;No\u0026quot;\u003c/span\u003e: \u003cspan class=pl-c1\u003e0\u003c/span\u003e}","\u003cspan class=pl-s1\u003ecalc_map\u003c/span\u003e \u003cspan class=pl-c1\u003e=\u003c/span\u003e {\u003cspan class=pl-s\u003e\u0026quot;No\u0026quot;\u003c/span\u003e: \u003cspan class=pl-c1\u003e0\u003c/span\u003e, \u003cspan class=pl-s\u003e\u0026quot;Sometimes\u0026quot;\u003c/span\u003e: \u003cspan class=pl-c1\u003e1\u003c/span\u003e, \u003cspan class=pl-s\u003e\u0026quot;Frequently\u0026quot;\u003c/span\u003e: \u003cspan class=pl-c1\u003e2\u003c/span\u003e}","\u003cspan class=pl-s1\u003emtrans_map\u003c/span\u003e \u003cspan class=pl-c1\u003e=\u003c/span\u003e {\u003cspan class=pl-s\u003e\u0026quot;Public_Transportation\u0026quot;\u003c/span\u003e: \u003cspan class=pl-c1\u003e0\u003c/span\u003e, \u003cspan class=pl-s\u003e\u0026quot;Walking\u0026quot;\u003c/span\u003e: \u003cspan class=pl-c1\u003e1\u003c/span\u003e, \u003cspan class=pl-s\u003e\u0026quot;Automobile\u0026quot;\u003c/span\u003e: \u003cspan class=pl-c1\u003e2\u003c/span\u003e, \u003cspan class=pl-s\u003e\u0026quot;Motorbike\u0026quot;\u003c/span\u003e: \u003cspan class=pl-c1\u003e3\u003c/span\u003e, \u003cspan class=pl-s\u003e\u0026quot;Bike\u0026quot;\u003c/span\u003e: \u003cspan class=pl-c1\u003e4\u003c/span\u003e}","","\u003cspan class=pl-c\u003e# Gabungkan input\u003c/span\u003e","\u003cspan class=pl-s1\u003edata\u003c/span\u003e \u003cspan class=pl-c1\u003e=\u003c/span\u003e \u003cspan class=pl-s1\u003enp\u003c/span\u003e.\u003cspan class=pl-c1\u003earray\u003c/span\u003e([[","    \u003cspan class=pl-s1\u003eage\u003c/span\u003e,","    \u003cspan class=pl-s1\u003eheight\u003c/span\u003e,","    \u003cspan class=pl-s1\u003eweight\u003c/span\u003e,","    \u003cspan class=pl-s1\u003efcvc\u003c/span\u003e,","    \u003cspan class=pl-s1\u003encp\u003c/span\u003e,","    \u003cspan class=pl-s1\u003ech2o\u003c/span\u003e,","    \u003cspan class=pl-s1\u003efaf\u003c/span\u003e,","    \u003cspan class=pl-s1\u003etue\u003c/span\u003e,","    \u003cspan class=pl-en\u003eencode\u003c/span\u003e(\u003cspan class=pl-s1\u003egender\u003c/span\u003e, \u003cspan class=pl-s1\u003egender_map\u003c/span\u003e),","    \u003cspan class=pl-en\u003eencode\u003c/span\u003e(\u003cspan class=pl-s1\u003efamily_history\u003c/span\u003e, \u003cspan class=pl-s1\u003efamily_map\u003c/span\u003e),","    \u003cspan class=pl-en\u003eencode\u003c/span\u003e(\u003cspan class=pl-s1\u003efavc\u003c/span\u003e, \u003cspan class=pl-s1\u003efavc_map\u003c/span\u003e),","    \u003cspan class=pl-en\u003eencode\u003c/span\u003e(\u003cspan class=pl-s1\u003ecaec\u003c/span\u003e, \u003cspan class=pl-s1\u003ecaec_map\u003c/span\u003e),","    \u003cspan class=pl-en\u003eencode\u003c/span\u003e(\u003cspan class=pl-s1\u003esmoke\u003c/span\u003e, \u003cspan class=pl-s1\u003esmoke_map\u003c/span\u003e),","    \u003cspan class=pl-en\u003eencode\u003c/span\u003e(\u003cspan class=pl-s1\u003escc\u003c/span\u003e, \u003cspan class=pl-s1\u003escc_map\u003c/span\u003e),","    \u003cspan class=pl-en\u003eencode\u003c/span\u003e(\u003cspan class=pl-s1\u003ecalc\u003c/span\u003e, \u003cspan class=pl-s1\u003ecalc_map\u003c/span\u003e),","    \u003cspan class=pl-en\u003eencode\u003c/span\u003e(\u003cspan class=pl-s1\u003emtrans\u003c/span\u003e, \u003cspan class=pl-s1\u003emtrans_map\u003c/span\u003e)","]])","","\u003cspan class=pl-c\u003e# Tombol prediksi\u003c/span\u003e","\u003cspan class=pl-k\u003eif\u003c/span\u003e \u003cspan class=pl-s1\u003est\u003c/span\u003e.\u003cspan class=pl-c1\u003ebutton\u003c/span\u003e(\u003cspan class=pl-s\u003e\u0026quot;Prediksi\u0026quot;\u003c/span\u003e):","    \u003cspan class=pl-s1\u003edata_scaled\u003c/span\u003e \u003cspan class=pl-c1\u003e=\u003c/span\u003e \u003cspan class=pl-s1\u003escaler\u003c/span\u003e.\u003cspan class=pl-c1\u003etransform\u003c/span\u003e(\u003cspan class=pl-s1\u003edata\u003c/span\u003e)","    \u003cspan class=pl-s1\u003epred\u003c/span\u003e \u003cspan class=pl-c1\u003e=\u003c/span\u003e \u003cspan class=pl-s1\u003emodel\u003c/span\u003e.\u003cspan class=pl-c1\u003epredict\u003c/span\u003e(\u003cspan class=pl-s1\u003edata_scaled\u003c/span\u003e)[\u003cspan class=pl-c1\u003e0\u003c/span\u003e]","    ","    \u003cspan class=pl-s1\u003eklasifikasi\u003c/span\u003e \u003cspan class=pl-c1\u003e=\u003c/span\u003e {","        \u003cspan class=pl-c1\u003e0\u003c/span\u003e: \u003cspan class=pl-s\u003e\u0026quot;Berat Badan Kurang\u0026quot;\u003c/span\u003e,","        \u003cspan class=pl-c1\u003e1\u003c/span\u003e: \u003cspan class=pl-s\u003e\u0026quot;Berat Badan Normal\u0026quot;\u003c/span\u003e,","        \u003cspan class=pl-c1\u003e2\u003c/span\u003e: \u003cspan class=pl-s\u003e\u0026quot;Kelebihan Berat Badan Tingkat I\u0026quot;\u003c/span\u003e,","        \u003cspan class=pl-c1\u003e3\u003c/span\u003e: \u003cspan class=pl-s\u003e\u0026quot;Kelebihan Berat Badan Tingkat II\u0026quot;\u003c/span\u003e,","        \u003cspan class=pl-c1\u003e4\u003c/span\u003e: \u003cspan class=pl-s\u003e\u0026quot;Obesitas Tipe I\u0026quot;\u003c/span\u003e,","        \u003cspan class=pl-c1\u003e5\u003c/span\u003e: \u003cspan class=pl-s\u003e\u0026quot;Obesitas Tipe II\u0026quot;\u003c/span\u003e,","        \u003cspan class=pl-c1\u003e6\u003c/span\u003e: \u003cspan class=pl-s\u003e\u0026quot;Obesitas Tipe III\u0026quot;\u003c/span\u003e","    }","    \u003cspan class=pl-s1\u003est\u003c/span\u003e.\u003cspan class=pl-c1\u003esuccess\u003c/span\u003e(\u003cspan class=pl-s\u003ef\u0026quot;Hasil Prediksi: **\u003cspan class=pl-s1\u003e\u003cspan class=pl-kos\u003e{\u003c/span\u003e\u003cspan class=pl-s1\u003eklasifikasi\u003c/span\u003e[\u003cspan class=pl-s1\u003epred\u003c/span\u003e]\u003cspan class=pl-kos\u003e}\u003c/span\u003e\u003c/span\u003e**\u0026quot;\u003c/span\u003e)"],"csv":null,"csvError":null,"dependabotInfo":{"showConfigurationBanner":false,"configFilePath":null,"networkDependabotPath":"/fastabyq/-Deploy_ke_Streamlit_Cloud/network/updates","dismissConfigurationNoticePath":"/settings/dismiss-notice/dependabot_configuration_notice","configurationNoticeDismissed":false},"displayName":"app.py","displayUrl":"https://github.com/fastabyq/-Deploy_ke_Streamlit_Cloud/blob/main/app.py?raw=true","headerInfo":{"blobSize":"2.71 KB","deleteTooltip":"Fork this repository and delete the file","editTooltip":"Fork this repository and edit the file","ghDesktopPath":"https://desktop.github.com","isGitLfs":false,"onBranch":true,"shortPath":"8bdc9c1","siteNavLoginPath":"/login?return_to=https%3A%2F%2Fgithub.com%2Ffastabyq%2F-Deploy_ke_Streamlit_Cloud%2Fblob%2Fmain%2Fapp.py","isCSV":false,"isRichtext":false,"toc":null,"lineInfo":{"truncatedLoc":"80","truncatedSloc":"71"},"mode":"file"},"image":false,"isCodeownersFile":null,"isPlain":false,"isValidLegacyIssueTemplate":false,"issueTemplate":null,"discussionTemplate":null,"language":"Python","languageID":303,"large":false,"planSupportInfo":{"repoIsFork":null,"repoOwnedByCurrentUser":null,"requestFullPath":"/fastabyq/-Deploy_ke_Streamlit_Cloud/blob/main/app.py","showFreeOrgGatedFeatureMessage":null,"showPlanSupportBanner":null,"upgradeDataAttributes":null,"upgradePath":null},"publishBannersInfo":{"dismissActionNoticePath":"/settings/dismiss-notice/publish_action_from_dockerfile","releasePath":"/fastabyq/-Deploy_ke_Streamlit_Cloud/releases/new?marketplace=true","showPublishActionBanner":false},"rawBlobUrl":"https://github.com/fastabyq/-Deploy_ke_Streamlit_Cloud/raw/refs/heads/main/app.py","renderImageOrRaw":false,"richText":null,"renderedFileInfo":null,"shortPath":null,"symbolsEnabled":true,"tabSize":8,"topBannersInfo":{"overridingGlobalFundingFile":false,"globalPreferredFundingPath":null,"showInvalidCitationWarning":false,"citationHelpUrl":"https://docs.github.com/github/creating-cloning-and-archiving-repositories/creating-a-repository-on-github/about-citation-files","actionsOnboardingTip":null},"truncated":false,"viewable":true,"workflowRedirectUrl":null,"symbols":{"timed_out":false,"not_analyzed":false,"symbols":[{"name":"model","kind":"constant","ident_start":86,"ident_end":91,"extent_start":86,"extent_end":127,"fully_qualified_name":"model","ident_utf16":{"start":{"line_number":5,"utf16_col":0},"end":{"line_number":5,"utf16_col":5}},"extent_utf16":{"start":{"line_number":5,"utf16_col":0},"end":{"line_number":5,"utf16_col":41}}},{"name":"scaler","kind":"constant","ident_start":129,"ident_end":135,"extent_start":129,"extent_end":163,"fully_qualified_name":"scaler","ident_utf16":{"start":{"line_number":6,"utf16_col":0},"end":{"line_number":6,"utf16_col":6}},"extent_utf16":{"start":{"line_number":6,"utf16_col":0},"end":{"line_number":6,"utf16_col":34}}},{"name":"age","kind":"constant","ident_start":314,"ident_end":317,"extent_start":314,"extent_end":356,"fully_qualified_name":"age","ident_utf16":{"start":{"line_number":13,"utf16_col":0},"end":{"line_number":13,"utf16_col":3}},"extent_utf16":{"start":{"line_number":13,"utf16_col":0},"end":{"line_number":13,"utf16_col":42}}},{"name":"height","kind":"constant","ident_start":358,"ident_end":364,"extent_start":358,"extent_end":422,"fully_qualified_name":"height","ident_utf16":{"start":{"line_number":14,"utf16_col":0},"end":{"line_number":14,"utf16_col":6}},"extent_utf16":{"start":{"line_number":14,"utf16_col":0},"end":{"line_number":14,"utf16_col":64}}},{"name":"weight","kind":"constant","ident_start":424,"ident_end":430,"extent_start":424,"extent_end":481,"fully_qualified_name":"weight","ident_utf16":{"start":{"line_number":15,"utf16_col":0},"end":{"line_number":15,"utf16_col":6}},"extent_utf16":{"start":{"line_number":15,"utf16_col":0},"end":{"line_number":15,"utf16_col":57}}},{"name":"fcvc","kind":"constant","ident_start":483,"ident_end":487,"extent_start":483,"extent_end":533,"fully_qualified_name":"fcvc","ident_utf16":{"start":{"line_number":16,"utf16_col":0},"end":{"line_number":16,"utf16_col":4}},"extent_utf16":{"start":{"line_number":16,"utf16_col":0},"end":{"line_number":16,"utf16_col":50}}},{"name":"ncp","kind":"constant","ident_start":535,"ident_end":538,"extent_start":535,"extent_end":590,"fully_qualified_name":"ncp","ident_utf16":{"start":{"line_number":17,"utf16_col":0},"end":{"line_number":17,"utf16_col":3}},"extent_utf16":{"start":{"line_number":17,"utf16_col":0},"end":{"line_number":17,"utf16_col":55}}},{"name":"ch2o","kind":"constant","ident_start":592,"ident_end":596,"extent_start":592,"extent_end":637,"fully_qualified_name":"ch2o","ident_utf16":{"start":{"line_number":18,"utf16_col":0},"end":{"line_number":18,"utf16_col":4}},"extent_utf16":{"start":{"line_number":18,"utf16_col":0},"end":{"line_number":18,"utf16_col":45}}},{"name":"faf","kind":"constant","ident_start":639,"ident_end":642,"extent_start":639,"extent_end":688,"fully_qualified_name":"faf","ident_utf16":{"start":{"line_number":19,"utf16_col":0},"end":{"line_number":19,"utf16_col":3}},"extent_utf16":{"start":{"line_number":19,"utf16_col":0},"end":{"line_number":19,"utf16_col":49}}},{"name":"tue","kind":"constant","ident_start":690,"ident_end":693,"extent_start":690,"extent_end":745,"fully_qualified_name":"tue","ident_utf16":{"start":{"line_number":20,"utf16_col":0},"end":{"line_number":20,"utf16_col":3}},"extent_utf16":{"start":{"line_number":20,"utf16_col":0},"end":{"line_number":20,"utf16_col":55}}},{"name":"gender","kind":"constant","ident_start":770,"ident_end":776,"extent_start":770,"extent_end":828,"fully_qualified_name":"gender","ident_utf16":{"start":{"line_number":23,"utf16_col":0},"end":{"line_number":23,"utf16_col":6}},"extent_utf16":{"start":{"line_number":23,"utf16_col":0},"end":{"line_number":23,"utf16_col":58}}},{"name":"family_history","kind":"constant","ident_start":830,"ident_end":844,"extent_start":830,"extent_end":903,"fully_qualified_name":"family_history","ident_utf16":{"start":{"line_number":24,"utf16_col":0},"end":{"line_number":24,"utf16_col":14}},"extent_utf16":{"start":{"line_number":24,"utf16_col":0},"end":{"line_number":24,"utf16_col":73}}},{"name":"favc","kind":"constant","ident_start":905,"ident_end":909,"extent_start":905,"extent_end":981,"fully_qualified_name":"favc","ident_utf16":{"start":{"line_number":25,"utf16_col":0},"end":{"line_number":25,"utf16_col":4}},"extent_utf16":{"start":{"line_number":25,"utf16_col":0},"end":{"line_number":25,"utf16_col":76}}},{"name":"caec","kind":"constant","ident_start":983,"ident_end":987,"extent_start":983,"extent_end":1068,"fully_qualified_name":"caec","ident_utf16":{"start":{"line_number":26,"utf16_col":0},"end":{"line_number":26,"utf16_col":4}},"extent_utf16":{"start":{"line_number":26,"utf16_col":0},"end":{"line_number":26,"utf16_col":85}}},{"name":"smoke","kind":"constant","ident_start":1070,"ident_end":1075,"extent_start":1070,"extent_end":1117,"fully_qualified_name":"smoke","ident_utf16":{"start":{"line_number":27,"utf16_col":0},"end":{"line_number":27,"utf16_col":5}},"extent_utf16":{"start":{"line_number":27,"utf16_col":0},"end":{"line_number":27,"utf16_col":47}}},{"name":"scc","kind":"constant","ident_start":1119,"ident_end":1122,"extent_start":1119,"extent_end":1174,"fully_qualified_name":"scc","ident_utf16":{"start":{"line_number":28,"utf16_col":0},"end":{"line_number":28,"utf16_col":3}},"extent_utf16":{"start":{"line_number":28,"utf16_col":0},"end":{"line_number":28,"utf16_col":55}}},{"name":"calc","kind":"constant","ident_start":1176,"ident_end":1180,"extent_start":1176,"extent_end":1251,"fully_qualified_name":"calc","ident_utf16":{"start":{"line_number":29,"utf16_col":0},"end":{"line_number":29,"utf16_col":4}},"extent_utf16":{"start":{"line_number":29,"utf16_col":0},"end":{"line_number":29,"utf16_col":75}}},{"name":"mtrans","kind":"constant","ident_start":1253,"ident_end":1259,"extent_start":1253,"extent_end":1363,"fully_qualified_name":"mtrans","ident_utf16":{"start":{"line_number":30,"utf16_col":0},"end":{"line_number":30,"utf16_col":6}},"extent_utf16":{"start":{"line_number":30,"utf16_col":0},"end":{"line_number":30,"utf16_col":110}}},{"name":"encode","kind":"function","ident_start":1453,"ident_end":1459,"extent_start":1449,"extent_end":1506,"fully_qualified_name":"encode","ident_utf16":{"start":{"line_number":33,"utf16_col":4},"end":{"line_number":33,"utf16_col":10}},"extent_utf16":{"start":{"line_number":33,"utf16_col":0},"end":{"line_number":34,"utf16_col":30}}},{"name":"gender_map","kind":"constant","ident_start":1510,"ident_end":1520,"extent_start":1510,"extent_end":1547,"fully_qualified_name":"gender_map","ident_utf16":{"start":{"line_number":36,"utf16_col":0},"end":{"line_number":36,"utf16_col":10}},"extent_utf16":{"start":{"line_number":36,"utf16_col":0},"end":{"line_number":36,"utf16_col":37}}},{"name":"family_map","kind":"constant","ident_start":1549,"ident_end":1559,"extent_start":1549,"extent_end":1581,"fully_qualified_name":"family_map","ident_utf16":{"start":{"line_number":37,"utf16_col":0},"end":{"line_number":37,"utf16_col":10}},"extent_utf16":{"start":{"line_number":37,"utf16_col":0},"end":{"line_number":37,"utf16_col":32}}},{"name":"favc_map","kind":"constant","ident_start":1583,"ident_end":1591,"extent_start":1583,"extent_end":1613,"fully_qualified_name":"favc_map","ident_utf16":{"start":{"line_number":38,"utf16_col":0},"end":{"line_number":38,"utf16_col":8}},"extent_utf16":{"start":{"line_number":38,"utf16_col":0},"end":{"line_number":38,"utf16_col":30}}},{"name":"caec_map","kind":"constant","ident_start":1615,"ident_end":1623,"extent_start":1615,"extent_end":1681,"fully_qualified_name":"caec_map","ident_utf16":{"start":{"line_number":39,"utf16_col":0},"end":{"line_number":39,"utf16_col":8}},"extent_utf16":{"start":{"line_number":39,"utf16_col":0},"end":{"line_number":39,"utf16_col":66}}},{"name":"smoke_map","kind":"constant","ident_start":1683,"ident_end":1692,"extent_start":1683,"extent_end":1714,"fully_qualified_name":"smoke_map","ident_utf16":{"start":{"line_number":40,"utf16_col":0},"end":{"line_number":40,"utf16_col":9}},"extent_utf16":{"start":{"line_number":40,"utf16_col":0},"end":{"line_number":40,"utf16_col":31}}},{"name":"scc_map","kind":"constant","ident_start":1716,"ident_end":1723,"extent_start":1716,"extent_end":1745,"fully_qualified_name":"scc_map","ident_utf16":{"start":{"line_number":41,"utf16_col":0},"end":{"line_number":41,"utf16_col":7}},"extent_utf16":{"start":{"line_number":41,"utf16_col":0},"end":{"line_number":41,"utf16_col":29}}},{"name":"calc_map","kind":"constant","ident_start":1747,"ident_end":1755,"extent_start":1747,"extent_end":1800,"fully_qualified_name":"calc_map","ident_utf16":{"start":{"line_number":42,"utf16_col":0},"end":{"line_number":42,"utf16_col":8}},"extent_utf16":{"start":{"line_number":42,"utf16_col":0},"end":{"line_number":42,"utf16_col":53}}},{"name":"mtrans_map","kind":"constant","ident_start":1802,"ident_end":1812,"extent_start":1802,"extent_end":1901,"fully_qualified_name":"mtrans_map","ident_utf16":{"start":{"line_number":43,"utf16_col":0},"end":{"line_number":43,"utf16_col":10}},"extent_utf16":{"start":{"line_number":43,"utf16_col":0},"end":{"line_number":43,"utf16_col":99}}},{"name":"data","kind":"constant","ident_start":1924,"ident_end":1928,"extent_start":1924,"extent_end":2286,"fully_qualified_name":"data","ident_utf16":{"start":{"line_number":46,"utf16_col":0},"end":{"line_number":46,"utf16_col":4}},"extent_utf16":{"start":{"line_number":46,"utf16_col":0},"end":{"line_number":63,"utf16_col":3}}}]}},"copilotInfo":null,"copilotAccessAllowed":true,"modelsAccessAllowed":false,"modelsRepoIntegrationEnabled":false,"csrf_tokens":{"/fastabyq/-Deploy_ke_Streamlit_Cloud/branches":{"post":"3B72F0Xd80THSHpsFG_Ji2391B9RfYS3dRbnxfpNDieGpT4TBDWPappDeX91pexuW4D97afPDX9RuHilrgaa6A"},"/repos/preferences":{"post":"jgchNonRyuh-IJ8MB_wrIVS79kIA9nMwsVxRN1g13DH3gR-k9kNLCjqvr5Rt9Ful8ZLOsHRpB3ASOiwBs-Pr4w"}}},"title":"-Deploy_ke_Streamlit_Cloud/app.py at main · fastabyq/-Deploy_ke_Streamlit_Cloud","appPayload":{"helpUrl":"https://docs.github.com","findFileWorkerPath":"/assets-cdn/worker/find-file-worker-263cab1760dd.js","findInFileWorkerPath":"/assets-cdn/worker/find-in-file-worker-1b17b3e7786a.js","githubDevUrl":"https://github.dev/","enabled_features":{"code_nav_ui_events":false,"react_blob_overlay":true,"accessible_code_button":true}}}</script>
  <div data-target="react-app.reactRoot"><meta data-hydrostats="publish"> <!-- --> <!-- --> <button hidden="" data-testid="header-permalink-button" data-hotkey-scope="read-only-cursor-text-area" data-hotkey="y,Shift+Y"></button><button hidden="" data-hotkey="y,Shift+Y"></button><div><div style="--spacing:var(--spacing-none)" class="prc-PageLayout-PageLayoutRoot-1zlEO"><div class="prc-PageLayout-PageLayoutWrapper-s2ao4" data-width="full"><div class="prc-PageLayout-PageLayoutContent-jzDMn"><div tabindex="0" class="Box-sc-g0xbh4-0 gISSDQ"><div class="prc-PageLayout-PaneWrapper-nGO0U ReposFileTreePane-module__Pane--wS7IV ReposFileTreePane-module__HidePane--Gj4XZ" style="--offset-header:0px;--spacing-row:var(--spacing-none);--spacing-column:var(--spacing-none)" data-is-hidden="false" data-position="start" data-sticky="true"><div class="prc-PageLayout-HorizontalDivider-CYLp5 prc-PageLayout-PaneHorizontalDivider-4exOb" data-variant="none" data-position="start" style="--spacing-divider:var(--spacing-none);--spacing:var(--spacing-none)"></div><div class="prc-PageLayout-Pane-Vl5LI" data-resizable="true" style="--spacing:var(--spacing-none);--pane-min-width:256px;--pane-max-width:calc(100vw - var(--pane-max-width-diff));--pane-width-size:var(--pane-width-large);--pane-width:320px"><div><div id="repos-file-tree" class="Box-sc-g0xbh4-0 bNhwaa"><div class="ReposFileTreePane-module__Box_1--Bz4Aw"><div class="Box-sc-g0xbh4-0 jfIeyl"><h2 class="use-tree-pane-module__Heading--DlnQ2 prc-Heading-Heading-6CmGO"><button data-component="IconButton" type="button" data-testid="collapse-file-tree-button" aria-expanded="true" aria-controls="repos-file-tree" class="prc-Button-ButtonBase-c50BI position-relative ExpandFileTreeButton-module__expandButton--gL4is fgColor-muted prc-Button-IconButton-szpyj" data-loading="false" data-no-visuals="true" data-size="medium" data-variant="invisible" aria-describedby=":R756mplab:-loading-announcement" aria-labelledby=":R156mplab:" data-hotkey="Control+b"><svg aria-hidden="true" focusable="false" class="octicon octicon-sidebar-expand" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="m4.177 7.823 2.396-2.396A.25.25 0 0 1 7 5.604v4.792a.25.25 0 0 1-.427.177L4.177 8.177a.25.25 0 0 1 0-.354Z"></path><path d="M0 1.75C0 .784.784 0 1.75 0h12.5C15.216 0 16 .784 16 1.75v12.5A1.75 1.75 0 0 1 14.25 16H1.75A1.75 1.75 0 0 1 0 14.25Zm1.75-.25a.25.25 0 0 0-.25.25v12.5c0 .138.112.25.25.25H9.5v-13Zm12.5 13a.25.25 0 0 0 .25-.25V1.75a.25.25 0 0 0-.25-.25H11v13Z"></path></svg></button><span class="prc-TooltipV2-Tooltip-cYMVY" data-direction="se" aria-hidden="true" id=":R156mplab:" popover="auto">Collapse file tree</span><button hidden="" data-testid="" data-hotkey-scope="read-only-cursor-text-area" data-hotkey="Control+b"></button></h2><h2 class="Box-sc-g0xbh4-0 kOkWgo prc-Heading-Heading-6CmGO">Files</h2></div><div class="ReposFileTreePane-module__Box_2--uC_pl"><div class="ReposFileTreePane-module__Box_3--Tgoja"><button type="button" aria-haspopup="true" aria-expanded="false" tabindex="0" aria-label="main branch" data-testid="anchor-button" class="Box-sc-g0xbh4-0 JMXqM prc-Button-ButtonBase-c50BI react-repos-tree-pane-ref-selector width-full ref-selector-class" data-loading="false" data-size="medium" data-variant="default" aria-describedby="branch-picker-repos-header-ref-selector-loading-announcement" id="branch-picker-repos-header-ref-selector" data-hotkey="w"><span data-component="buttonContent" class="Box-sc-g0xbh4-0 gUkoLg prc-Button-ButtonContent-HKbr-"><span data-component="text" class="prc-Button-Label-pTQ3x"><div class="Box-sc-g0xbh4-0 bZBlpz"><div class="Box-sc-g0xbh4-0 bJjzmO"><svg aria-hidden="true" focusable="false" class="octicon octicon-git-branch" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M9.5 3.25a2.25 2.25 0 1 1 3 2.122V6A2.5 2.5 0 0 1 10 8.5H6a1 1 0 0 0-1 1v1.128a2.251 2.251 0 1 1-1.5 0V5.372a2.25 2.25 0 1 1 1.5 0v1.836A2.493 2.493 0 0 1 6 7h4a1 1 0 0 0 1-1v-.628A2.25 2.25 0 0 1 9.5 3.25Zm-6 0a.75.75 0 1 0 1.5 0 .75.75 0 0 0-1.5 0Zm8.25-.75a.75.75 0 1 0 0 1.5.75.75 0 0 0 0-1.5ZM4.25 12a.75.75 0 1 0 0 1.5.75.75 0 0 0 0-1.5Z"></path></svg></div><div class="Box-sc-g0xbh4-0 ffLUq ref-selector-button-text-container"><span class="Box-sc-g0xbh4-0 bmcJak prc-Text-Text-0ima0">&nbsp;<!-- -->main</span></div></div></span><span data-component="trailingVisual" class="prc-Button-Visual-2epfX prc-Button-VisualWrap-Db-eB"><svg aria-hidden="true" focusable="false" class="octicon octicon-triangle-down" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="m4.427 7.427 3.396 3.396a.25.25 0 0 0 .354 0l3.396-3.396A.25.25 0 0 0 11.396 7H4.604a.25.25 0 0 0-.177.427Z"></path></svg></span></span></button><button hidden="" data-hotkey-scope="read-only-cursor-text-area" data-hotkey="w"></button></div><div class="ReposFileTreePane-module__Box_4--brBpx"><a data-component="IconButton" type="button" class="prc-Button-ButtonBase-c50BI ReposFileTreePane-module__IconButton--tNSTv prc-Button-IconButton-szpyj" data-loading="false" data-no-visuals="true" data-size="medium" data-variant="default" aria-describedby=":R6q6mplab:-loading-announcement" aria-labelledby=":Rq6mplab:" href="https://github.com/fastabyq/-Deploy_ke_Streamlit_Cloud/new/main"><svg aria-hidden="true" focusable="false" class="octicon octicon-plus" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path></svg></a><span class="prc-TooltipV2-Tooltip-cYMVY" data-direction="n" aria-hidden="true" id=":Rq6mplab:" popover="auto">Add file</span><button data-component="IconButton" type="button" class="Box-sc-g0xbh4-0 dPUXSa prc-Button-ButtonBase-c50BI SearchButton-module__IconButton--LGy8b prc-Button-IconButton-szpyj" data-loading="false" data-no-visuals="true" data-size="medium" data-variant="default" aria-describedby=":Rra6mplab:-loading-announcement" aria-labelledby=":R3a6mplab:" data-hotkey="/"><svg aria-hidden="true" focusable="false" class="octicon octicon-search" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M10.68 11.74a6 6 0 0 1-7.922-8.982 6 6 0 0 1 8.982 7.922l3.04 3.04a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215ZM11.5 7a4.499 4.499 0 1 0-8.997 0A4.499 4.499 0 0 0 11.5 7Z"></path></svg></button><span class="prc-TooltipV2-Tooltip-cYMVY" data-direction="nw" aria-hidden="true" id=":R3a6mplab:" popover="auto">Search this repository</span><button hidden="" data-testid="" data-hotkey-scope="read-only-cursor-text-area" data-hotkey="/"></button></div></div></div><div class="Box-sc-g0xbh4-0 ReposFileTreePane-module__FileResultsList--t38MI FileResultsList-module__Box_1--ZnWjQ"><span class="FileResultsList-module__FilesSearchBox--J5FtW FilesSearchBox-module__TextInput--LKpMn TextInput-wrapper prc-components-TextInputWrapper-i1ofR prc-components-TextInputBaseWrapper-ueK9q" data-leading-visual="true" data-trailing-visual="true" aria-busy="false"><span class="TextInput-icon" id=":R5amplab:" aria-hidden="true"><svg aria-hidden="true" focusable="false" class="octicon octicon-search" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M10.68 11.74a6 6 0 0 1-7.922-8.982 6 6 0 0 1 8.982 7.922l3.04 3.04a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215ZM11.5 7a4.499 4.499 0 1 0-8.997 0A4.499 4.499 0 0 0 11.5 7Z"></path></svg></span><input type="text" aria-label="Go to file" role="combobox" aria-controls="file-results-list" aria-expanded="false" aria-haspopup="dialog" autocorrect="off" spellcheck="false" placeholder="Go to file" aria-describedby=":R5amplab: :R5amplabH1:" data-component="input" class="prc-components-Input-Ic-y8" value=""><span class="TextInput-icon" id=":R5amplabH1:" aria-hidden="true"><div class="FilesSearchBox-module__Box--Ye6rL"><kbd>t</kbd></div></span></span></div><button hidden="" data-testid="" data-hotkey-scope="read-only-cursor-text-area" data-hotkey="t,Shift+T"></button><button hidden="" data-hotkey="t,Shift+T"></button><div class="Box-sc-g0xbh4-0 ReposFileTreePane-module__Box_5--tQNH_"><div><div class="react-tree-show-tree-items"><div class="ReposFileTreeView-module__Box--V2jWA" data-testid="repos-file-tree-container"><nav aria-label="File Tree Navigation"><span role="status" aria-live="polite" aria-atomic="true" class="_VisuallyHidden__VisuallyHidden-sc-11jhm7a-0 brGdpi"></span><ul role="tree" aria-label="Files" data-truncate-text="true" class="prc-TreeView-TreeViewRootUlStyles-eZtxW"><li class="PRIVATE_TreeView-item prc-TreeView-TreeViewItem-ShJr0" tabindex="-1" id="README.md-item" role="treeitem" aria-labelledby=":r11:" aria-describedby=":r12:" aria-level="1" aria-selected="false"><div class="PRIVATE_TreeView-item-container prc-TreeView-TreeViewItemContainer--2Rkn" style="--level: 1; content-visibility: auto; contain-intrinsic-size: auto 2rem;"><div style="grid-area: spacer; display: flex;"><div style="width: 100%; display: flex;"></div></div><div id=":r11:" class="PRIVATE_TreeView-item-content prc-TreeView-TreeViewItemContent-f0r0b"><div class="PRIVATE_VisuallyHidden prc-TreeView-TreeViewVisuallyHidden-4-mPv" aria-hidden="true" id=":r12:"></div><div class="PRIVATE_TreeView-item-visual prc-TreeView-TreeViewItemVisual-dRlGq" aria-hidden="true"><svg aria-hidden="true" focusable="false" class="octicon octicon-file" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align: text-bottom;"><path d="M2 1.75C2 .784 2.784 0 3.75 0h6.586c.464 0 .909.184 1.237.513l2.914 2.914c.329.328.513.773.513 1.237v9.586A1.75 1.75 0 0 1 13.25 16h-9.5A1.75 1.75 0 0 1 2 14.25Zm1.75-.25a.25.25 0 0 0-.25.25v12.5c0 .138.112.25.25.25h9.5a.25.25 0 0 0 .25-.25V6h-2.75A1.75 1.75 0 0 1 9 4.25V1.5Zm6.75.062V4.25c0 .138.112.25.25.25h2.688l-.011-.013-2.914-2.914-.013-.011Z"></path></svg></div><span class="PRIVATE_TreeView-item-content-text prc-TreeView-TreeViewItemContentText-smZM-"><span>README.md</span></span></div></div></li><li class="PRIVATE_TreeView-item prc-TreeView-TreeViewItem-ShJr0" tabindex="0" id="app.py-item" role="treeitem" aria-labelledby=":r14:" aria-describedby=":r15:" aria-level="1" aria-selected="false" aria-current="true"><div class="PRIVATE_TreeView-item-container prc-TreeView-TreeViewItemContainer--2Rkn" style="--level: 1;"><div style="grid-area: spacer; display: flex;"><div style="width: 100%; display: flex;"></div></div><div id=":r14:" class="PRIVATE_TreeView-item-content prc-TreeView-TreeViewItemContent-f0r0b"><div class="PRIVATE_VisuallyHidden prc-TreeView-TreeViewVisuallyHidden-4-mPv" aria-hidden="true" id=":r15:"></div><div class="PRIVATE_TreeView-item-visual prc-TreeView-TreeViewItemVisual-dRlGq" aria-hidden="true"><svg aria-hidden="true" focusable="false" class="octicon octicon-file" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align: text-bottom;"><path d="M2 1.75C2 .784 2.784 0 3.75 0h6.586c.464 0 .909.184 1.237.513l2.914 2.914c.329.328.513.773.513 1.237v9.586A1.75 1.75 0 0 1 13.25 16h-9.5A1.75 1.75 0 0 1 2 14.25Zm1.75-.25a.25.25 0 0 0-.25.25v12.5c0 .138.112.25.25.25h9.5a.25.25 0 0 0 .25-.25V6h-2.75A1.75 1.75 0 0 1 9 4.25V1.5Zm6.75.062V4.25c0 .138.112.25.25.25h2.688l-.011-.013-2.914-2.914-.013-.011Z"></path></svg></div><span class="PRIVATE_TreeView-item-content-text prc-TreeView-TreeViewItemContentText-smZM-"><span>app.py</span></span></div></div></li><li class="PRIVATE_TreeView-item prc-TreeView-TreeViewItem-ShJr0" tabindex="-1" id="model_obesitas.pkl-item" role="treeitem" aria-labelledby=":r17:" aria-describedby=":r18:" aria-level="1" aria-selected="false"><div class="PRIVATE_TreeView-item-container prc-TreeView-TreeViewItemContainer--2Rkn" style="--level: 1; content-visibility: auto; contain-intrinsic-size: auto 2rem;"><div style="grid-area: spacer; display: flex;"><div style="width: 100%; display: flex;"></div></div><div id=":r17:" class="PRIVATE_TreeView-item-content prc-TreeView-TreeViewItemContent-f0r0b"><div class="PRIVATE_VisuallyHidden prc-TreeView-TreeViewVisuallyHidden-4-mPv" aria-hidden="true" id=":r18:"></div><div class="PRIVATE_TreeView-item-visual prc-TreeView-TreeViewItemVisual-dRlGq" aria-hidden="true"><svg aria-hidden="true" focusable="false" class="octicon octicon-file" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align: text-bottom;"><path d="M2 1.75C2 .784 2.784 0 3.75 0h6.586c.464 0 .909.184 1.237.513l2.914 2.914c.329.328.513.773.513 1.237v9.586A1.75 1.75 0 0 1 13.25 16h-9.5A1.75 1.75 0 0 1 2 14.25Zm1.75-.25a.25.25 0 0 0-.25.25v12.5c0 .138.112.25.25.25h9.5a.25.25 0 0 0 .25-.25V6h-2.75A1.75 1.75 0 0 1 9 4.25V1.5Zm6.75.062V4.25c0 .138.112.25.25.25h2.688l-.011-.013-2.914-2.914-.013-.011Z"></path></svg></div><span class="PRIVATE_TreeView-item-content-text prc-TreeView-TreeViewItemContentText-smZM-"><span>model_obesitas.pkl</span></span></div></div></li><li class="PRIVATE_TreeView-item prc-TreeView-TreeViewItem-ShJr0" tabindex="-1" id="requirements.txt-item" role="treeitem" aria-labelledby=":r1a:" aria-describedby=":r1b:" aria-level="1" aria-selected="false"><div class="PRIVATE_TreeView-item-container prc-TreeView-TreeViewItemContainer--2Rkn" style="--level: 1; content-visibility: auto; contain-intrinsic-size: auto 2rem;"><div style="grid-area: spacer; display: flex;"><div style="width: 100%; display: flex;"></div></div><div id=":r1a:" class="PRIVATE_TreeView-item-content prc-TreeView-TreeViewItemContent-f0r0b"><div class="PRIVATE_VisuallyHidden prc-TreeView-TreeViewVisuallyHidden-4-mPv" aria-hidden="true" id=":r1b:"></div><div class="PRIVATE_TreeView-item-visual prc-TreeView-TreeViewItemVisual-dRlGq" aria-hidden="true"><svg aria-hidden="true" focusable="false" class="octicon octicon-file" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align: text-bottom;"><path d="M2 1.75C2 .784 2.784 0 3.75 0h6.586c.464 0 .909.184 1.237.513l2.914 2.914c.329.328.513.773.513 1.237v9.586A1.75 1.75 0 0 1 13.25 16h-9.5A1.75 1.75 0 0 1 2 14.25Zm1.75-.25a.25.25 0 0 0-.25.25v12.5c0 .138.112.25.25.25h9.5a.25.25 0 0 0 .25-.25V6h-2.75A1.75 1.75 0 0 1 9 4.25V1.5Zm6.75.062V4.25c0 .138.112.25.25.25h2.688l-.011-.013-2.914-2.914-.013-.011Z"></path></svg></div><span class="PRIVATE_TreeView-item-content-text prc-TreeView-TreeViewItemContentText-smZM-"><span>requirements.txt</span></span></div></div></li><li class="PRIVATE_TreeView-item prc-TreeView-TreeViewItem-ShJr0" tabindex="-1" id="scaler.pkl-item" role="treeitem" aria-labelledby=":r1d:" aria-describedby=":r1e:" aria-level="1" aria-selected="false"><div class="PRIVATE_TreeView-item-container prc-TreeView-TreeViewItemContainer--2Rkn" style="--level: 1; content-visibility: auto; contain-intrinsic-size: auto 2rem;"><div style="grid-area: spacer; display: flex;"><div style="width: 100%; display: flex;"></div></div><div id=":r1d:" class="PRIVATE_TreeView-item-content prc-TreeView-TreeViewItemContent-f0r0b"><div class="PRIVATE_VisuallyHidden prc-TreeView-TreeViewVisuallyHidden-4-mPv" aria-hidden="true" id=":r1e:"></div><div class="PRIVATE_TreeView-item-visual prc-TreeView-TreeViewItemVisual-dRlGq" aria-hidden="true"><svg aria-hidden="true" focusable="false" class="octicon octicon-file" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align: text-bottom;"><path d="M2 1.75C2 .784 2.784 0 3.75 0h6.586c.464 0 .909.184 1.237.513l2.914 2.914c.329.328.513.773.513 1.237v9.586A1.75 1.75 0 0 1 13.25 16h-9.5A1.75 1.75 0 0 1 2 14.25Zm1.75-.25a.25.25 0 0 0-.25.25v12.5c0 .138.112.25.25.25h9.5a.25.25 0 0 0 .25-.25V6h-2.75A1.75 1.75 0 0 1 9 4.25V1.5Zm6.75.062V4.25c0 .138.112.25.25.25h2.688l-.011-.013-2.914-2.914-.013-.011Z"></path></svg></div><span class="PRIVATE_TreeView-item-content-text prc-TreeView-TreeViewItemContentText-smZM-"><span>scaler.pkl</span></span></div></div></li></ul></nav></div></div></div></div></div></div></div><div class="prc-PageLayout-VerticalDivider-4A4Qm prc-PageLayout-PaneVerticalDivider-1c9vy" data-variant="line" data-position="start" style="--spacing:var(--spacing-none)"><div role="slider" aria-label="Draggable pane splitter" aria-valuemin="256" aria-valuemax="473" aria-valuenow="320" aria-valuetext="Pane width 320 pixels" tabindex="0" class="Box-sc-g0xbh4-0 fFMzrG"></div></div></div></div><div class="prc-PageLayout-ContentWrapper-b-QRo CodeView-module__SplitPageLayout_Content--qxR1C" data-is-hidden="false"><div class="prc-PageLayout-Content--F7-I" data-width="full" style="--spacing:var(--spacing-none)"><div data-selector="repos-split-pane-content" tabindex="0" class="Box-sc-g0xbh4-0 leYMvG"><div class="Box-sc-g0xbh4-0 KMPzq"><div class="container CodeViewHeader-module__Box--PofRM"><div class="px-3 pt-3 pb-0" id="StickyHeader" style="position: sticky;"><div class="CodeViewHeader-module__Box_1--KpLzV"><div class="CodeViewHeader-module__Box_2--xzDOt"><div class="CodeViewHeader-module__Box_6--iStzT"><div class="Box-sc-g0xbh4-0 cEytCf"><nav data-testid="breadcrumbs" aria-labelledby="repos-header-breadcrumb--wide-heading" id="repos-header-breadcrumb--wide" class="Box-sc-g0xbh4-0 fzFXnm"><h2 class="sr-only ScreenReaderHeading-module__userSelectNone--vW4Cq prc-Heading-Heading-6CmGO" data-testid="screen-reader-heading" id="repos-header-breadcrumb--wide-heading">Breadcrumbs</h2><ol class="Box-sc-g0xbh4-0 iMnkmv"><li class="Box-sc-g0xbh4-0 ghzDag"><a class="Box-sc-g0xbh4-0 kHuKdh prc-Link-Link-85e08" sx="[object Object]" data-testid="breadcrumbs-repo-link" href="https://github.com/fastabyq/-Deploy_ke_Streamlit_Cloud/tree/main">-Deploy_ke_Streamlit_Cloud</a></li></ol></nav><div data-testid="breadcrumbs-filename" class="Box-sc-g0xbh4-0 ghzDag"><span class="Box-sc-g0xbh4-0 hXyrdx prc-Text-Text-0ima0" aria-hidden="true">/</span><h1 class="Box-sc-g0xbh4-0 jGhzSQ prc-Heading-Heading-6CmGO" tabindex="-1" id="file-name-id-wide">app.py</h1></div><button data-component="IconButton" type="button" class="prc-Button-ButtonBase-c50BI ml-2 prc-Button-IconButton-szpyj" data-loading="false" data-no-visuals="true" data-size="small" data-variant="invisible" aria-describedby=":Rvb9lab:-loading-announcement" aria-labelledby=":R3b9lab:"><svg aria-hidden="true" focusable="false" class="octicon octicon-copy" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M0 6.75C0 5.784.784 5 1.75 5h1.5a.75.75 0 0 1 0 1.5h-1.5a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-1.5a.75.75 0 0 1 1.5 0v1.5A1.75 1.75 0 0 1 9.25 16h-7.5A1.75 1.75 0 0 1 0 14.25Z"></path><path d="M5 1.75C5 .784 5.784 0 6.75 0h7.5C15.216 0 16 .784 16 1.75v7.5A1.75 1.75 0 0 1 14.25 11h-7.5A1.75 1.75 0 0 1 5 9.25Zm1.75-.25a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-7.5a.25.25 0 0 0-.25-.25Z"></path></svg></button><span class="CopyToClipboardButton-module__tooltip--Dq1IB prc-TooltipV2-Tooltip-cYMVY" data-direction="nw" aria-label="Copy path" aria-hidden="true" id=":R3b9lab:" popover="auto">Copy path</span></div></div><div class="react-code-view-header-element--wide"><div class="CodeViewHeader-module__Box_7--FZfkg"><div class="d-flex gap-2"> <button hidden="" data-testid="" data-hotkey="l,Shift+L" data-hotkey-scope="read-only-cursor-text-area"></button><button hidden="" data-hotkey="l,Shift+L"></button><button hidden="" data-testid="" data-hotkey="Mod+Alt+g" data-hotkey-scope="read-only-cursor-text-area"></button><button hidden="" data-hotkey="Mod+Alt+g"></button><button type="button" data-hotkey="b,Shift+B,Control+/ Control+b" class="Box-sc-g0xbh4-0 fjrFuv prc-Button-ButtonBase-c50BI NavigationMenu-module__Button--SJihq" data-loading="false" data-no-visuals="true" data-size="medium" data-variant="default" aria-describedby=":r3e:-loading-announcement"><span data-component="buttonContent" class="Box-sc-g0xbh4-0 gUkoLg prc-Button-ButtonContent-HKbr-"><span data-component="text" class="prc-Button-Label-pTQ3x">Blame</span></span></button><button hidden="" data-testid="" data-hotkey="b,Shift+B,Control+/ Control+b" data-hotkey-scope="read-only-cursor-text-area"></button><button data-component="IconButton" type="button" data-testid="more-file-actions-button-nav-menu-wide" aria-haspopup="true" aria-expanded="false" tabindex="0" class="prc-Button-ButtonBase-c50BI js-blob-dropdown-click NavigationMenu-module__IconButton--NqJ_L prc-Button-IconButton-szpyj" data-loading="false" data-no-visuals="true" data-size="medium" data-variant="default" aria-describedby=":Rihj9lab:-loading-announcement" aria-labelledby=":Rfihj9lab:" id=":Rihj9lab:"><svg aria-hidden="true" focusable="false" class="octicon octicon-kebab-horizontal" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M8 9a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3ZM1.5 9a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3Zm13 0a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3Z"></path></svg></button><span class="prc-TooltipV2-Tooltip-cYMVY" data-direction="nw" aria-hidden="true" id=":Rfihj9lab:" popover="auto">More file actions</span> </div></div></div><div class="react-code-view-header-element--narrow"><div class="CodeViewHeader-module__Box_7--FZfkg"><div class="d-flex gap-2"> <button hidden="" data-testid="" data-hotkey="l,Shift+L" data-hotkey-scope="read-only-cursor-text-area"></button><button hidden="" data-hotkey="l,Shift+L"></button><button hidden="" data-testid="" data-hotkey="Mod+Alt+g" data-hotkey-scope="read-only-cursor-text-area"></button><button hidden="" data-hotkey="Mod+Alt+g"></button><button type="button" data-hotkey="b,Shift+B,Control+/ Control+b" class="Box-sc-g0xbh4-0 fjrFuv prc-Button-ButtonBase-c50BI NavigationMenu-module__Button--SJihq" data-loading="false" data-no-visuals="true" data-size="medium" data-variant="default" aria-describedby=":r3f:-loading-announcement"><span data-component="buttonContent" class="Box-sc-g0xbh4-0 gUkoLg prc-Button-ButtonContent-HKbr-"><span data-component="text" class="prc-Button-Label-pTQ3x">Blame</span></span></button><button hidden="" data-testid="" data-hotkey="b,Shift+B,Control+/ Control+b" data-hotkey-scope="read-only-cursor-text-area"></button><button data-component="IconButton" type="button" data-testid="more-file-actions-button-nav-menu-narrow" aria-haspopup="true" aria-expanded="false" tabindex="0" class="prc-Button-ButtonBase-c50BI js-blob-dropdown-click NavigationMenu-module__IconButton--NqJ_L prc-Button-IconButton-szpyj" data-loading="false" data-no-visuals="true" data-size="medium" data-variant="default" aria-describedby=":Rihr9lab:-loading-announcement" aria-labelledby=":Rfihr9lab:" id=":Rihr9lab:"><svg aria-hidden="true" focusable="false" class="octicon octicon-kebab-horizontal" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M8 9a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3ZM1.5 9a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3Zm13 0a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3Z"></path></svg></button><span class="prc-TooltipV2-Tooltip-cYMVY" data-direction="nw" aria-hidden="true" id=":Rfihr9lab:" popover="auto">More file actions</span> </div></div></div></div></div></div></div></div><div class="Box-sc-g0xbh4-0 dJxjrT react-code-view-bottom-padding"> <div class="BlobTopBanners-module__Box--g_bGk"></div> <!-- --> <!-- --> </div><div class="Box-sc-g0xbh4-0 dJxjrT"> <!-- --> <!-- --> <button hidden="" data-testid="" data-hotkey="r,Shift+R" data-hotkey-scope="read-only-cursor-text-area"></button><button hidden="" data-hotkey="r,Shift+R"></button><div class="d-flex flex-column border rounded-2 mb-3 pl-1"><div class="LatestCommit-module__Box--En0AE"><h2 class="sr-only ScreenReaderHeading-module__userSelectNone--vW4Cq prc-Heading-Heading-6CmGO" data-testid="screen-reader-heading">Latest commit</h2><div data-testid="latest-commit" class="LatestCommit-module__Box_1--Kkzat"><div class="Box-sc-g0xbh4-0 dpBUfI"><div data-testid="author-avatar" class="Box-sc-g0xbh4-0 hKWjvQ"><a class="prc-Link-Link-85e08" href="https://github.com/fastabyq" data-testid="avatar-icon-link" data-hovercard-url="/users/fastabyq/hovercard"><img data-component="Avatar" class="Box-sc-g0xbh4-0 cvdqJW prc-Avatar-Avatar-ZRS-m" alt="fastabyq" width="20" height="20" src="./app_files/171785532" data-testid="github-avatar" aria-label="fastabyq" style="--avatarSize-regular: 20px;"></a><a class="Box-sc-g0xbh4-0 kJvqaq prc-Link-Link-85e08" data-muted="true" href="https://github.com/fastabyq/-Deploy_ke_Streamlit_Cloud/commits?author=fastabyq" aria-label="commits by fastabyq" data-hovercard-url="/users/fastabyq/hovercard">fastabyq</a></div><span class=""></span></div><div class="d-none d-sm-flex LatestCommit-module__Box_2--gAJMD"><div class="Truncate flex-items-center f5"><span class="Truncate-text prc-Text-Text-0ima0" data-testid="latest-commit-html"><a href="https://github.com/fastabyq/-Deploy_ke_Streamlit_Cloud/commit/f9dfa36bb7753b1aba5a17b6408a54e940f3979a" class="Link--secondary" data-pjax="true" data-hovercard-url="/fastabyq/-Deploy_ke_Streamlit_Cloud/commit/f9dfa36bb7753b1aba5a17b6408a54e940f3979a/hovercard">Add files via upload</a></span></div></div><span class="d-flex d-sm-none fgColor-muted f6"><relative-time class="sc-aXZVg" tense="past" datetime="2025-06-02T03:58:29.000Z" title="Jun 1, 2025, 8:58 PM PDT"><template shadowrootmode="open">2 weeks ago</template>Jun 1, 2025</relative-time></span></div><div class="d-flex flex-shrink-0 gap-2"><div data-testid="latest-commit-details" class="d-none d-sm-flex flex-items-center"><span class="d-flex flex-nowrap fgColor-muted f6"><a class="Link--secondary prc-Link-Link-85e08" aria-label="Commit f9dfa36" data-hovercard-url="/fastabyq/-Deploy_ke_Streamlit_Cloud/commit/f9dfa36bb7753b1aba5a17b6408a54e940f3979a/hovercard" href="https://github.com/fastabyq/-Deploy_ke_Streamlit_Cloud/commit/f9dfa36bb7753b1aba5a17b6408a54e940f3979a" data-discover="true">f9dfa36</a>&nbsp;·&nbsp;<relative-time class="sc-aXZVg" tense="past" datetime="2025-06-02T03:58:29.000Z" title="Jun 1, 2025, 8:58 PM PDT"><template shadowrootmode="open">2 weeks ago</template>Jun 1, 2025</relative-time></span></div><div class="d-flex gap-2"><h2 class="sr-only ScreenReaderHeading-module__userSelectNone--vW4Cq prc-Heading-Heading-6CmGO" data-testid="screen-reader-heading">History</h2><a href="https://github.com/fastabyq/-Deploy_ke_Streamlit_Cloud/commits/main/app.py" class="prc-Button-ButtonBase-c50BI d-none d-lg-flex LinkButton-module__code-view-link-button--xvCGA flex-items-center fgColor-default" data-loading="false" data-size="small" data-variant="invisible" aria-describedby=":R1bdal9lab:-loading-announcement"><span data-component="buttonContent" data-align="center" class="prc-Button-ButtonContent-HKbr-"><span data-component="leadingVisual" class="prc-Button-Visual-2epfX prc-Button-VisualWrap-Db-eB"><svg aria-hidden="true" focusable="false" class="octicon octicon-history" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="m.427 1.927 1.215 1.215a8.002 8.002 0 1 1-1.6 5.685.75.75 0 1 1 1.493-.154 6.5 6.5 0 1 0 1.18-4.458l1.358 1.358A.25.25 0 0 1 3.896 6H.25A.25.25 0 0 1 0 5.75V2.104a.25.25 0 0 1 .427-.177ZM7.75 4a.75.75 0 0 1 .75.75v2.992l2.028.812a.75.75 0 0 1-.557 1.392l-2.5-1A.751.751 0 0 1 7 8.25v-3.5A.75.75 0 0 1 7.75 4Z"></path></svg></span><span data-component="text" class="prc-Button-Label-pTQ3x"><span class="fgColor-default">History</span></span></span></a><div class="d-sm-none"><button data-component="IconButton" type="button" aria-pressed="false" aria-expanded="false" data-testid="latest-commit-details-toggle" class="prc-Button-ButtonBase-c50BI LatestCommit-module__IconButton--jJLCx prc-Button-IconButton-szpyj" data-loading="false" data-no-visuals="true" data-size="small" data-variant="invisible" aria-describedby=":r3j:-loading-announcement" aria-labelledby=":r3i:"><svg aria-hidden="true" focusable="false" class="octicon octicon-ellipsis" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align: text-bottom;"><path d="M0 5.75C0 4.784.784 4 1.75 4h12.5c.966 0 1.75.784 1.75 1.75v4.5A1.75 1.75 0 0 1 14.25 12H1.75A1.75 1.75 0 0 1 0 10.25ZM12 7a1 1 0 1 0 0 2 1 1 0 0 0 0-2ZM7 8a1 1 0 1 0 2 0 1 1 0 0 0-2 0ZM4 7a1 1 0 1 0 0 2 1 1 0 0 0 0-2Z"></path></svg></button><span class="prc-TooltipV2-Tooltip-cYMVY" data-direction="s" aria-hidden="true" id=":r3i:" popover="auto">Open commit details</span></div><div class="d-flex d-lg-none"><span role="tooltip" aria-label="History" id="history-icon-button-tooltip" class="Tooltip__TooltipBase-sc-17tf59c-0 fiSvBN tooltipped-n"><a href="https://github.com/fastabyq/-Deploy_ke_Streamlit_Cloud/commits/main/app.py" class="prc-Button-ButtonBase-c50BI LinkButton-module__code-view-link-button--xvCGA flex-items-center fgColor-default" data-loading="false" data-size="small" data-variant="invisible" aria-describedby=":R6bdal9lab:-loading-announcement history-icon-button-tooltip"><span data-component="buttonContent" data-align="center" class="prc-Button-ButtonContent-HKbr-"><span data-component="leadingVisual" class="prc-Button-Visual-2epfX prc-Button-VisualWrap-Db-eB"><svg aria-hidden="true" focusable="false" class="octicon octicon-history" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="m.427 1.927 1.215 1.215a8.002 8.002 0 1 1-1.6 5.685.75.75 0 1 1 1.493-.154 6.5 6.5 0 1 0 1.18-4.458l1.358 1.358A.25.25 0 0 1 3.896 6H.25A.25.25 0 0 1 0 5.75V2.104a.25.25 0 0 1 .427-.177ZM7.75 4a.75.75 0 0 1 .75.75v2.992l2.028.812a.75.75 0 0 1-.557 1.392l-2.5-1A.751.751 0 0 1 7 8.25v-3.5A.75.75 0 0 1 7.75 4Z"></path></svg></span></span></a></span></div></div></div></div></div><div class="Box-sc-g0xbh4-0 ldRxiI"><div class="Box-sc-g0xbh4-0 fVkfyA container"><div class="Box-sc-g0xbh4-0 gNAmSV react-code-size-details-banner"><div class="react-code-size-details-banner CodeSizeDetails-module__Box--QdxnQ"><div class="text-mono CodeSizeDetails-module__Box_1--_uFDs"><div title="2.71 KB" data-testid="blob-size" class="Truncate__StyledTruncate-sc-23o1d2-0 bgsFir CodeSizeDetails-module__Truncate_1--er0Uk"><span>80 lines (71 loc) · 2.71 KB</span></div></div></div></div><div class="Box-sc-g0xbh4-0 jdLMhu react-blob-view-header-sticky" id="repos-sticky-header"><div class="BlobViewHeader-module__Box--pvsIA"><div class="react-blob-sticky-header"><div class="Box-sc-g0xbh4-0 hqwSEx"><div class="FileNameStickyHeader-module__Box_5--xBJ2J"><div class="Box-sc-g0xbh4-0 fHind"><nav data-testid="breadcrumbs" aria-labelledby="sticky-breadcrumb-heading" id="sticky-breadcrumb" class="Box-sc-g0xbh4-0 fzFXnm"><h2 class="sr-only ScreenReaderHeading-module__userSelectNone--vW4Cq prc-Heading-Heading-6CmGO" data-testid="screen-reader-heading" id="sticky-breadcrumb-heading">Breadcrumbs</h2><ol class="Box-sc-g0xbh4-0 iMnkmv"><li class="Box-sc-g0xbh4-0 ghzDag"><a class="Box-sc-g0xbh4-0 kHuKdh prc-Link-Link-85e08" sx="[object Object]" data-testid="breadcrumbs-repo-link" href="https://github.com/fastabyq/-Deploy_ke_Streamlit_Cloud/tree/main">-Deploy_ke_Streamlit_Cloud</a></li></ol></nav><div data-testid="breadcrumbs-filename" class="Box-sc-g0xbh4-0 ghzDag"><span class="Box-sc-g0xbh4-0 bQeXnn prc-Text-Text-0ima0" aria-hidden="true">/</span><h1 class="Box-sc-g0xbh4-0 dnZoUW prc-Heading-Heading-6CmGO" tabindex="-1" id="sticky-file-name-id">app.py</h1></div></div><button type="button" class="prc-Button-ButtonBase-c50BI FileNameStickyHeader-module__Button--SaiiH FileNameStickyHeader-module__GoToTopButton--9lB4x" data-loading="false" data-size="small" data-variant="invisible" aria-describedby=":R4mfal9lab:-loading-announcement"><span data-component="buttonContent" data-align="center" class="prc-Button-ButtonContent-HKbr-"><span data-component="leadingVisual" class="prc-Button-Visual-2epfX prc-Button-VisualWrap-Db-eB"><svg aria-hidden="true" focusable="false" class="octicon octicon-arrow-up" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M3.47 7.78a.75.75 0 0 1 0-1.06l4.25-4.25a.75.75 0 0 1 1.06 0l4.25 4.25a.751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018L9 4.81v7.44a.75.75 0 0 1-1.5 0V4.81L4.53 7.78a.75.75 0 0 1-1.06 0Z"></path></svg></span><span data-component="text" class="prc-Button-Label-pTQ3x">Top</span></span></button></div></div></div><div class="Box-sc-g0xbh4-0 gFKFyc BlobViewHeader-module__Box_1--PPihg"><h2 class="sr-only ScreenReaderHeading-module__userSelectNone--vW4Cq prc-Heading-Heading-6CmGO" data-testid="screen-reader-heading">File metadata and controls</h2><div class="BlobViewHeader-module__Box_2--G_jCG"><ul aria-label="File view" class="prc-SegmentedControl-SegmentedControl-e7570 BlobTabButtons-module__SegmentedControl--JMGov" data-size="small"><li class="prc-SegmentedControl-Item-7Aq6h" data-selected=""><button aria-current="true" class="prc-SegmentedControl-Button-ojWXD" type="button" style="--separator-color:transparent" data-hotkey="Control+/ Control+c"><span class="prc-SegmentedControl-Content-gnQ4n segmentedControl-content"><div class="prc-SegmentedControl-Text-c5gSh segmentedControl-text" data-text="Code">Code</div></span></button></li><li class="prc-SegmentedControl-Item-7Aq6h"><button aria-current="false" class="prc-SegmentedControl-Button-ojWXD" type="button" style="--separator-color:var(--borderColor-default, var(--color-border-default, #30363d))" data-hotkey="b,Shift+B,Control+/ Control+b"><span class="prc-SegmentedControl-Content-gnQ4n segmentedControl-content"><div class="prc-SegmentedControl-Text-c5gSh segmentedControl-text" data-text="Blame">Blame</div></span></button></li></ul><button hidden="" data-testid="" data-hotkey-scope="read-only-cursor-text-area" data-hotkey="Control+/ Control+c"></button><button hidden="" data-testid="" data-hotkey-scope="read-only-cursor-text-area" data-hotkey="b,Shift+B,Control+/ Control+b"></button><div class="react-code-size-details-in-header CodeSizeDetails-module__Box--QdxnQ"><div class="text-mono CodeSizeDetails-module__Box_1--_uFDs"><div title="2.71 KB" data-testid="blob-size" class="Truncate__StyledTruncate-sc-23o1d2-0 bgsFir CodeSizeDetails-module__Truncate_1--er0Uk"><span>80 lines (71 loc) · 2.71 KB</span></div></div></div></div><div class="BlobViewHeader-module__Box_3--Kvpex"><button hidden="" data-testid="" data-hotkey="Control+Shift+&gt;" data-hotkey-scope="read-only-cursor-text-area"></button><button hidden="" data-hotkey="Control+Shift+&gt;"></button><button hidden="" data-testid="" data-hotkey="Control+Shift+&lt;" data-hotkey-scope="read-only-cursor-text-area"></button><button hidden="" data-hotkey="Control+Shift+&lt;"></button><div class="Box-sc-g0xbh4-0 pr-0 prc-ButtonGroup-ButtonGroup-vcMeG"><div><button data-component="IconButton" type="button" data-testid="copilot-ask-menu" class="prc-Button-ButtonBase-c50BI AskCopilotButton-module__square--o8kDO prc-Button-IconButton-szpyj" data-loading="false" data-no-visuals="true" data-size="small" data-variant="default" aria-describedby="blob-view-header-copilot-icon-loading-announcement" aria-labelledby=":R2v6fal9lab:" id="blob-view-header-copilot-icon"><svg aria-hidden="true" focusable="false" class="octicon octicon-copilot" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M7.998 15.035c-4.562 0-7.873-2.914-7.998-3.749V9.338c.085-.628.677-1.686 1.588-2.065.013-.07.024-.143.036-.218.029-.183.06-.384.126-.612-.201-.508-.254-1.084-.254-1.656 0-.87.128-1.769.693-2.484.579-.733 1.494-1.124 2.724-1.261 1.206-.134 2.262.034 2.944.765.05.053.096.108.139.165.044-.057.094-.112.143-.165.682-.731 1.738-.899 2.944-.765 1.23.137 2.145.528 2.724 1.261.566.715.693 1.614.693 2.484 0 .572-.053 1.148-.254 1.656.066.228.098.429.126.612.012.076.024.148.037.218.924.385 1.522 1.471 1.591 2.095v1.872c0 .766-3.351 3.795-8.002 3.795Zm0-1.485c2.28 0 4.584-1.11 5.002-1.433V7.862l-.023-.116c-.49.21-1.075.291-1.727.291-1.146 0-2.059-.327-2.71-.991A3.222 3.222 0 0 1 8 6.303a3.24 3.24 0 0 1-.544.743c-.65.664-1.563.991-2.71.991-.652 0-1.236-.081-1.727-.291l-.023.116v4.255c.419.323 2.722 1.433 5.002 1.433ZM6.762 2.83c-.193-.206-.637-.413-1.682-.297-1.019.113-1.479.404-1.713.7-.247.312-.369.789-.369 1.554 0 .793.129 1.171.308 1.371.162.181.519.379 1.442.379.853 0 1.339-.235 1.638-.54.315-.322.527-.827.617-1.553.117-.935-.037-1.395-.241-1.614Zm4.155-.297c-1.044-.116-1.488.091-1.681.297-.204.219-.359.679-.242 1.614.091.726.303 1.231.618 1.553.299.305.784.54 1.638.54.922 0 1.28-.198 1.442-.379.179-.2.308-.578.308-1.371 0-.765-.123-1.242-.37-1.554-.233-.296-.693-.587-1.713-.7Z"></path><path d="M6.25 9.037a.75.75 0 0 1 .75.75v1.501a.75.75 0 0 1-1.5 0V9.787a.75.75 0 0 1 .75-.75Zm4.25.75v1.501a.75.75 0 0 1-1.5 0V9.787a.75.75 0 0 1 1.5 0Z"></path></svg></button><span class="prc-TooltipV2-Tooltip-cYMVY" data-direction="s" aria-hidden="true" id=":R2v6fal9lab:" popover="auto">Ask Copilot about this file</span></div><div></div></div><div class="react-blob-header-edit-and-raw-actions BlobViewHeader-module__Box_4--vFP89"><div class="Box-sc-g0xbh4-0 prc-ButtonGroup-ButtonGroup-vcMeG"><div><a href="https://github.com/fastabyq/-Deploy_ke_Streamlit_Cloud/raw/refs/heads/main/app.py" data-testid="raw-button" class="Box-sc-g0xbh4-0 lefpaC prc-Button-ButtonBase-c50BI BlobViewHeader-module__LinkButton--DMph4" data-loading="false" data-no-visuals="true" data-size="small" data-variant="default" aria-describedby=":R1b76fal9lab:-loading-announcement" data-hotkey="Control+/ Control+r"><span data-component="buttonContent" class="Box-sc-g0xbh4-0 gUkoLg prc-Button-ButtonContent-HKbr-"><span data-component="text" class="prc-Button-Label-pTQ3x">Raw</span></span></a></div><div><button data-component="IconButton" type="button" data-testid="copy-raw-button" class="prc-Button-ButtonBase-c50BI prc-Button-IconButton-szpyj" data-loading="false" data-no-visuals="true" data-size="small" data-variant="default" aria-describedby=":R1mb76fal9lab:-loading-announcement" aria-labelledby=":R6b76fal9lab:" data-hotkey="Control+Shift+C"><svg aria-hidden="true" focusable="false" class="octicon octicon-copy" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M0 6.75C0 5.784.784 5 1.75 5h1.5a.75.75 0 0 1 0 1.5h-1.5a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-1.5a.75.75 0 0 1 1.5 0v1.5A1.75 1.75 0 0 1 9.25 16h-7.5A1.75 1.75 0 0 1 0 14.25Z"></path><path d="M5 1.75C5 .784 5.784 0 6.75 0h7.5C15.216 0 16 .784 16 1.75v7.5A1.75 1.75 0 0 1 14.25 11h-7.5A1.75 1.75 0 0 1 5 9.25Zm1.75-.25a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-7.5a.25.25 0 0 0-.25-.25Z"></path></svg></button><span class="prc-TooltipV2-Tooltip-cYMVY" data-direction="n" aria-hidden="true" id=":R6b76fal9lab:" popover="auto">Copy raw file</span></div><div><button data-component="IconButton" type="button" data-testid="download-raw-button" class="Box-sc-g0xbh4-0 ivobqY prc-Button-ButtonBase-c50BI prc-Button-IconButton-szpyj" data-loading="false" data-no-visuals="true" data-size="small" data-variant="default" aria-describedby=":Rfb76fal9lab:-loading-announcement" aria-labelledby=":R3b76fal9lab:" data-hotkey="Control+Shift+S"><svg aria-hidden="true" focusable="false" class="octicon octicon-download" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M2.75 14A1.75 1.75 0 0 1 1 12.25v-2.5a.75.75 0 0 1 1.5 0v2.5c0 .138.112.25.25.25h10.5a.25.25 0 0 0 .25-.25v-2.5a.75.75 0 0 1 1.5 0v2.5A1.75 1.75 0 0 1 13.25 14Z"></path><path d="M7.25 7.689V2a.75.75 0 0 1 1.5 0v5.689l1.97-1.969a.749.749 0 1 1 1.06 1.06l-3.25 3.25a.749.749 0 0 1-1.06 0L4.22 6.78a.749.749 0 1 1 1.06-1.06l1.97 1.969Z"></path></svg></button><span class="prc-TooltipV2-Tooltip-cYMVY" data-direction="n" aria-hidden="true" id=":R3b76fal9lab:" popover="auto">Download raw file</span></div></div><button hidden="" data-testid="raw-button-shortcut" data-hotkey-scope="read-only-cursor-text-area" data-hotkey="Control+/ Control+r"></button><button hidden="" data-testid="copy-raw-button-shortcut" data-hotkey-scope="read-only-cursor-text-area" data-hotkey="Control+Shift+C"></button><button hidden="" data-testid="download-raw-button-shortcut" data-hotkey-scope="read-only-cursor-text-area" data-hotkey="Control+Shift+S"></button><a class="js-github-dev-shortcut d-none prc-Link-Link-85e08" href="https://github.dev/" data-hotkey="., Control+Shift+/"></a><button hidden="" data-testid="" data-hotkey-scope="read-only-cursor-text-area" data-hotkey="., Control+Shift+/"></button><a class="js-github-dev-new-tab-shortcut d-none prc-Link-Link-85e08" href="https://github.dev/" target="_blank" data-hotkey="Shift+.,Shift+&gt;,&gt;"></a><button hidden="" data-testid="" data-hotkey-scope="read-only-cursor-text-area" data-hotkey="Shift+.,Shift+&gt;,&gt;"></button><div class="Box-sc-g0xbh4-0 prc-ButtonGroup-ButtonGroup-vcMeG"><div><a sx="[object Object]" data-component="IconButton" type="button" data-testid="edit-button" class="Box-sc-g0xbh4-0 iCOsHh prc-Button-ButtonBase-c50BI BlobViewHeader-module__IconButton_1--MzNlL prc-Button-IconButton-szpyj" data-loading="false" data-no-visuals="true" data-size="small" data-variant="default" aria-describedby=":Rdl76fal9lab:-loading-announcement" aria-labelledby=":R1l76fal9lab:" href="https://github.com/fastabyq/-Deploy_ke_Streamlit_Cloud/edit/main/app.py" data-hotkey="e,Shift+E"><svg aria-hidden="true" focusable="false" class="octicon octicon-pencil" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M11.013 1.427a1.75 1.75 0 0 1 2.474 0l1.086 1.086a1.75 1.75 0 0 1 0 2.474l-8.61 8.61c-.21.21-.47.364-.756.445l-3.251.93a.75.75 0 0 1-.927-.928l.929-3.25c.081-.286.235-.547.445-.758l8.61-8.61Zm.176 4.823L9.75 4.81l-6.286 6.287a.253.253 0 0 0-.064.108l-.558 1.953 1.953-.558a.253.253 0 0 0 .108-.064Zm1.238-3.763a.25.25 0 0 0-.354 0L10.811 3.75l1.439 1.44 1.263-1.263a.25.25 0 0 0 0-.354Z"></path></svg></a><span class="prc-TooltipV2-Tooltip-cYMVY" data-direction="nw" aria-hidden="true" id=":R1l76fal9lab:" popover="auto">Fork this repository and edit the file</span></div><div><button data-component="IconButton" type="button" data-testid="more-edit-button" aria-haspopup="true" aria-expanded="false" tabindex="0" class="prc-Button-ButtonBase-c50BI prc-Button-IconButton-szpyj" data-loading="false" data-no-visuals="true" data-size="small" data-variant="default" aria-describedby=":R2l76fal9lab:-loading-announcement" aria-labelledby=":R1ul76fal9lab:" id=":R2l76fal9lab:"><svg aria-hidden="true" focusable="false" class="octicon octicon-triangle-down" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="m4.427 7.427 3.396 3.396a.25.25 0 0 0 .354 0l3.396-3.396A.25.25 0 0 0 11.396 7H4.604a.25.25 0 0 0-.177.427Z"></path></svg></button><span class="prc-TooltipV2-Tooltip-cYMVY" data-direction="nw" aria-hidden="true" id=":R1ul76fal9lab:" popover="auto">More edit options</span></div></div><button hidden="" data-testid="" data-hotkey="e,Shift+E" data-hotkey-scope="read-only-cursor-text-area"></button></div><button data-component="IconButton" type="button" aria-pressed="false" aria-expanded="false" aria-controls="symbols-pane" data-hotkey="Control+i" data-testid="symbols-button" class="prc-Button-ButtonBase-c50BI BlobViewHeader-module__IconButton_2--KDy6i prc-Button-IconButton-szpyj" data-loading="false" data-no-visuals="true" data-size="small" data-variant="invisible" aria-describedby="symbols-button-loading-announcement" aria-labelledby=":r3g:" id="symbols-button"><svg aria-hidden="true" focusable="false" class="octicon octicon-code-square" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align: text-bottom;"><path d="M0 1.75C0 .784.784 0 1.75 0h12.5C15.216 0 16 .784 16 1.75v12.5A1.75 1.75 0 0 1 14.25 16H1.75A1.75 1.75 0 0 1 0 14.25Zm1.75-.25a.25.25 0 0 0-.25.25v12.5c0 .138.112.25.25.25h12.5a.25.25 0 0 0 .25-.25V1.75a.25.25 0 0 0-.25-.25Zm7.47 3.97a.75.75 0 0 1 1.06 0l2 2a.75.75 0 0 1 0 1.06l-2 2a.749.749 0 0 1-1.275-.326.749.749 0 0 1 .215-.734L10.69 8 9.22 6.53a.75.75 0 0 1 0-1.06ZM6.78 6.53 5.31 8l1.47 1.47a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215l-2-2a.75.75 0 0 1 0-1.06l2-2a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042Z"></path></svg></button><span class="prc-TooltipV2-Tooltip-cYMVY" data-direction="nw" aria-hidden="true" id=":r3g:" popover="auto">Open symbols panel</span><div class="react-blob-header-edit-and-raw-actions-combined"><button data-component="IconButton" type="button" title="More file actions" data-testid="more-file-actions-button" aria-haspopup="true" aria-expanded="false" tabindex="0" class="prc-Button-ButtonBase-c50BI js-blob-dropdown-click BlobViewHeader-module__IconButton--uO1fA prc-Button-IconButton-szpyj" data-loading="false" data-no-visuals="true" data-size="small" data-variant="invisible" aria-describedby=":R5v6fal9lab:-loading-announcement" aria-labelledby=":R3tv6fal9lab:" id=":R5v6fal9lab:"><svg aria-hidden="true" focusable="false" class="octicon octicon-kebab-horizontal" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M8 9a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3ZM1.5 9a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3Zm13 0a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3Z"></path></svg></button><span class="prc-TooltipV2-Tooltip-cYMVY" data-direction="nw" aria-hidden="true" id=":R3tv6fal9lab:" popover="auto">Edit and raw actions</span></div></div></div></div><div></div></div><div class="Box-sc-g0xbh4-0 hycJXc"><section aria-labelledby="file-name-id-wide file-name-id-mobile" class="Box-sc-g0xbh4-0 dceWRL"><div class="Box-sc-g0xbh4-0 dGXHv"><div id="highlighted-line-menu-positioner" class="position-relative"><div id="copilot-button-positioner" class="Box-sc-g0xbh4-0 bpDFns"><div class="Box-sc-g0xbh4-0 iJOeCH"><div class="Box-sc-g0xbh4-0 eJSJhL"><div class="Box-sc-g0xbh4-0 goOzhF"><div aria-hidden="true" data-testid="navigation-cursor" class="Box-sc-g0xbh4-0 code-navigation-cursor" style="top: 0px; left: 92px;"> </div><button hidden="" data-testid="NavigationCursorEnter" data-hotkey="Control+Enter" data-hotkey-scope="read-only-cursor-text-area"></button><button hidden="" data-testid="NavigationCursorSetHighlightedLine" data-hotkey="Shift+J" data-hotkey-scope="read-only-cursor-text-area"></button><button hidden="" data-testid="NavigationCursorSetHighlightAndExpandMenu" data-hotkey="Alt+Shift+C,Alt+Shift+Ç" data-hotkey-scope="read-only-cursor-text-area"></button><button hidden="" data-testid="NavigationCursorPageDown" data-hotkey="PageDown" data-hotkey-scope="read-only-cursor-text-area"></button><button hidden="" data-testid="NavigationCursorPageUp" data-hotkey="PageUp" data-hotkey-scope="read-only-cursor-text-area"></button><button hidden="" data-testid="" data-hotkey="/" data-hotkey-scope="read-only-cursor-text-area"></button></div></div><textarea id="read-only-cursor-text-area" data-testid="read-only-cursor-text-area" aria-label="file content" aria-readonly="true" inputmode="none" tabindex="0" aria-multiline="true" aria-haspopup="false" data-gramm="false" data-gramm_editor="false" data-enable-grammarly="false" spellcheck="false" autocorrect="off" autocapitalize="off" autocomplete="off" data-ms-editor="false" class="react-blob-textarea react-blob-print-hide" style="resize: none; margin-top: -2px; padding-left: 92px; padding-right: 70px; width: 100%; background-color: unset; box-sizing: border-box; color: transparent; position: absolute; border: none; tab-size: 8; outline: none; overflow: auto hidden; height: 1620px; font-size: 12px; line-height: 20px; overflow-wrap: normal; overscroll-behavior-x: none; white-space: pre; z-index: 1;">import streamlit as st
import numpy as np
import joblib

# Load model dan scaler
model = joblib.load("model_obesitas.pkl")
scaler = joblib.load("scaler.pkl")

# Judul Aplikasi
st.title("Prediksi Tingkat Obesitas")
st.markdown("Masukkan data berikut untuk memprediksi tingkat obesitas:")

# Input data
age = st.number_input("Usia", 10, 100, 25)
height = st.number_input("Tinggi Badan (meter)", 1.0, 2.5, 1.70)
weight = st.number_input("Berat Badan (kg)", 30, 200, 70)
fcvc = st.slider("Konsumsi Sayur (FCVC)", 1, 3, 2)
ncp = st.slider("Jumlah Makan per Hari (NCP)", 1, 4, 3)
ch2o = st.slider("Minum Air (CH2O)", 1, 3, 2)
faf = st.slider("Aktivitas Fisik (FAF)", 0, 3, 1)
tue = st.slider("Waktu Pakai Teknologi (TUE)", 0, 3, 1)

# Fitur kategorikal
gender = st.selectbox("Jenis Kelamin", ["Male", "Female"])
family_history = st.selectbox("Riwayat Keluarga Obesitas", ["Yes", "No"])
favc = st.selectbox("Sering Konsumsi Makanan Tinggi Kalori?", ["Yes", "No"])
caec = st.selectbox("Konsumsi Camilan?", ["No", "Sometimes", "Frequently", "Always"])
smoke = st.selectbox("Merokok?", ["Yes", "No"])
scc = st.selectbox("Kendalikan Kalori?", ["Yes", "No"])
calc = st.selectbox("Konsumsi Alkohol?", ["No", "Sometimes", "Frequently"])
mtrans = st.selectbox("Transportasi", ["Public_Transportation", "Walking", "Automobile", "Motorbike", "Bike"])

# Encode kategorikal manual (harus sama dengan label encoder kamu saat training)
def encode(val, mapping):
    return mapping.get(val, 0)

gender_map = {"Male": 1, "Female": 0}
family_map = {"Yes": 1, "No": 0}
favc_map = {"Yes": 1, "No": 0}
caec_map = {"No": 0, "Sometimes": 1, "Frequently": 2, "Always": 3}
smoke_map = {"Yes": 1, "No": 0}
scc_map = {"Yes": 1, "No": 0}
calc_map = {"No": 0, "Sometimes": 1, "Frequently": 2}
mtrans_map = {"Public_Transportation": 0, "Walking": 1, "Automobile": 2, "Motorbike": 3, "Bike": 4}

# Gabungkan input
data = np.array([[
    age,
    height,
    weight,
    fcvc,
    ncp,
    ch2o,
    faf,
    tue,
    encode(gender, gender_map),
    encode(family_history, family_map),
    encode(favc, favc_map),
    encode(caec, caec_map),
    encode(smoke, smoke_map),
    encode(scc, scc_map),
    encode(calc, calc_map),
    encode(mtrans, mtrans_map)
]])

# Tombol prediksi
if st.button("Prediksi"):
    data_scaled = scaler.transform(data)
    pred = model.predict(data_scaled)[0]
    
    klasifikasi = {
        0: "Berat Badan Kurang",
        1: "Berat Badan Normal",
        2: "Kelebihan Berat Badan Tingkat I",
        3: "Kelebihan Berat Badan Tingkat II",
        4: "Obesitas Tipe I",
        5: "Obesitas Tipe II",
        6: "Obesitas Tipe III"
    }
    st.success(f"Hasil Prediksi: **{klasifikasi[pred]}**")</textarea><button hidden="" data-testid="" data-hotkey="Alt+F1,Control+Alt+˙,Control+Alt+h" data-hotkey-scope="read-only-cursor-text-area"></button><div class="Box-sc-g0xbh4-0 kHHiZS"><div tabindex="0" class="Box-sc-g0xbh4-0 jqUoVd"><div class="Box-sc-g0xbh4-0 hPNVpr react-code-file-contents" role="presentation" aria-hidden="true" data-tab-size="8" data-paste-markdown-skip="true" data-hpc="true"><div class="react-line-numbers-no-virtualization" style="pointer-events: auto; position: relative; z-index: 2;"><div class="react-no-virtualization-wrapper-lines"><div data-line-number="1" class="react-line-number react-code-text" style="padding-right: 16px;">1</div><div data-line-number="2" class="react-line-number react-code-text" style="padding-right: 16px;">2</div><div data-line-number="3" class="react-line-number react-code-text" style="padding-right: 16px;">3</div><div data-line-number="4" class="react-line-number react-code-text" style="padding-right: 16px;">4</div><div data-line-number="5" class="react-line-number react-code-text" style="padding-right: 16px;">5</div><div data-line-number="6" class="react-line-number react-code-text" style="padding-right: 16px;">6</div><div data-line-number="7" class="react-line-number react-code-text" style="padding-right: 16px;">7</div><div data-line-number="8" class="react-line-number react-code-text" style="padding-right: 16px;">8</div><div data-line-number="9" class="react-line-number react-code-text" style="padding-right: 16px;">9</div><div data-line-number="10" class="react-line-number react-code-text" style="padding-right: 16px;">10</div><div data-line-number="11" class="react-line-number react-code-text" style="padding-right: 16px;">11</div><div data-line-number="12" class="react-line-number react-code-text" style="padding-right: 16px;">12</div><div data-line-number="13" class="react-line-number react-code-text" style="padding-right: 16px;">13</div><div data-line-number="14" class="react-line-number react-code-text" style="padding-right: 16px;">14</div><div data-line-number="15" class="react-line-number react-code-text" style="padding-right: 16px;">15</div><div data-line-number="16" class="react-line-number react-code-text" style="padding-right: 16px;">16</div><div data-line-number="17" class="react-line-number react-code-text" style="padding-right: 16px;">17</div><div data-line-number="18" class="react-line-number react-code-text" style="padding-right: 16px;">18</div><div data-line-number="19" class="react-line-number react-code-text" style="padding-right: 16px;">19</div><div data-line-number="20" class="react-line-number react-code-text" style="padding-right: 16px;">20</div><div data-line-number="21" class="react-line-number react-code-text" style="padding-right: 16px;">21</div><div data-line-number="22" class="react-line-number react-code-text" style="padding-right: 16px;">22</div><div data-line-number="23" class="react-line-number react-code-text" style="padding-right: 16px;">23</div><div data-line-number="24" class="react-line-number react-code-text" style="padding-right: 16px;">24</div><div data-line-number="25" class="react-line-number react-code-text" style="padding-right: 16px;">25</div><div data-line-number="26" class="react-line-number react-code-text" style="padding-right: 16px;">26</div><div data-line-number="27" class="react-line-number react-code-text" style="padding-right: 16px;">27</div><div data-line-number="28" class="react-line-number react-code-text" style="padding-right: 16px;">28</div><div data-line-number="29" class="react-line-number react-code-text" style="padding-right: 16px;">29</div><div data-line-number="30" class="react-line-number react-code-text" style="padding-right: 16px;">30</div><div data-line-number="31" class="react-line-number react-code-text" style="padding-right: 16px;">31</div><div data-line-number="32" class="react-line-number react-code-text" style="padding-right: 16px;">32</div><div data-line-number="33" class="react-line-number react-code-text" style="padding-right: 16px;">33</div><div data-line-number="34" class="react-line-number react-code-text" style="padding-right: 16px;">34</div><div data-line-number="35" class="react-line-number react-code-text" style="padding-right: 16px;">35</div><div data-line-number="36" class="react-line-number react-code-text" style="padding-right: 16px;">36</div><div data-line-number="37" class="react-line-number react-code-text" style="padding-right: 16px;">37</div><div data-line-number="38" class="react-line-number react-code-text" style="padding-right: 16px;">38</div><div data-line-number="39" class="react-line-number react-code-text" style="padding-right: 16px;">39</div><div data-line-number="40" class="react-line-number react-code-text" style="padding-right: 16px;">40</div><div data-line-number="41" class="react-line-number react-code-text" style="padding-right: 16px;">41</div><div data-line-number="42" class="react-line-number react-code-text" style="padding-right: 16px;">42</div><div data-line-number="43" class="react-line-number react-code-text" style="padding-right: 16px;">43</div><div data-line-number="44" class="react-line-number react-code-text" style="padding-right: 16px;">44</div><div data-line-number="45" class="react-line-number react-code-text" style="padding-right: 16px;">45</div><div data-line-number="46" class="react-line-number react-code-text" style="padding-right: 16px;">46</div><div data-line-number="47" class="react-line-number react-code-text" style="padding-right: 16px;">47<span class="Box-sc-g0xbh4-0 cJGaMs"><div aria-label="Collapse code section" role="button" class="Box-sc-g0xbh4-0 iGLarr"><svg aria-hidden="true" focusable="false" class="octicon octicon-chevron-down Octicon-sc-9kayk9-0" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align: text-bottom;"><path d="M12.78 5.22a.749.749 0 0 1 0 1.06l-4.25 4.25a.749.749 0 0 1-1.06 0L3.22 6.28a.749.749 0 1 1 1.06-1.06L8 8.939l3.72-3.719a.749.749 0 0 1 1.06 0Z"></path></svg></div></span></div><div data-line-number="48" class="child-of-line-46  react-line-number react-code-text" style="padding-right: 16px;">48</div><div data-line-number="49" class="child-of-line-46  react-line-number react-code-text" style="padding-right: 16px;">49</div><div data-line-number="50" class="child-of-line-46  react-line-number react-code-text" style="padding-right: 16px;">50</div><div data-line-number="51" class="child-of-line-46  react-line-number react-code-text" style="padding-right: 16px;">51</div><div data-line-number="52" class="child-of-line-46  react-line-number react-code-text" style="padding-right: 16px;">52</div><div data-line-number="53" class="child-of-line-46  react-line-number react-code-text" style="padding-right: 16px;">53</div><div data-line-number="54" class="child-of-line-46  react-line-number react-code-text" style="padding-right: 16px;">54</div><div data-line-number="55" class="child-of-line-46  react-line-number react-code-text" style="padding-right: 16px;">55</div><div data-line-number="56" class="child-of-line-46  react-line-number react-code-text" style="padding-right: 16px;">56</div><div data-line-number="57" class="child-of-line-46  react-line-number react-code-text" style="padding-right: 16px;">57</div><div data-line-number="58" class="child-of-line-46  react-line-number react-code-text" style="padding-right: 16px;">58</div><div data-line-number="59" class="child-of-line-46  react-line-number react-code-text" style="padding-right: 16px;">59</div><div data-line-number="60" class="child-of-line-46  react-line-number react-code-text" style="padding-right: 16px;">60</div></div><div class="react-no-virtualization-wrapper-lines"><div data-line-number="61" class="child-of-line-46  react-line-number react-code-text" style="padding-right: 16px;">61</div><div data-line-number="62" class="child-of-line-46  react-line-number react-code-text" style="padding-right: 16px;">62</div><div data-line-number="63" class="child-of-line-46  react-line-number react-code-text" style="padding-right: 16px;">63</div><div data-line-number="64" class="react-line-number react-code-text" style="padding-right: 16px;">64</div><div data-line-number="65" class="react-line-number react-code-text" style="padding-right: 16px;">65</div><div data-line-number="66" class="react-line-number react-code-text" style="padding-right: 16px;">66</div><div data-line-number="67" class="react-line-number react-code-text" style="padding-right: 16px;">67</div><div data-line-number="68" class="react-line-number react-code-text" style="padding-right: 16px;">68</div><div data-line-number="69" class="react-line-number react-code-text" style="padding-right: 16px;">69</div><div data-line-number="70" class="react-line-number react-code-text" style="padding-right: 16px;">70</div><div data-line-number="71" class="react-line-number react-code-text" style="padding-right: 16px;">71</div><div data-line-number="72" class="react-line-number react-code-text" style="padding-right: 16px;">72</div><div data-line-number="73" class="react-line-number react-code-text" style="padding-right: 16px;">73</div><div data-line-number="74" class="react-line-number react-code-text" style="padding-right: 16px;">74</div><div data-line-number="75" class="react-line-number react-code-text" style="padding-right: 16px;">75</div><div data-line-number="76" class="react-line-number react-code-text" style="padding-right: 16px;">76</div><div data-line-number="77" class="react-line-number react-code-text" style="padding-right: 16px;">77</div><div data-line-number="78" class="react-line-number react-code-text" style="padding-right: 16px;">78</div><div data-line-number="79" class="react-line-number react-code-text" style="padding-right: 16px;">79</div><div data-line-number="80" class="react-line-number react-code-text" style="padding-right: 16px;">80</div></div></div><div class="react-code-lines"><div inert="inert"><div class="react-no-virtualization-wrapper"><div id="LC1" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div "><span class="pl-k">import</span> <span class="pl-s1">streamlit</span> <span class="pl-k">as</span> <span class="pl-s1">st</span></div>
<div id="LC2" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div "><span class="pl-k">import</span> <span class="pl-s1">numpy</span> <span class="pl-k">as</span> <span class="pl-s1">np</span></div>
<div id="LC3" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div "><span class="pl-k">import</span> <span class="pl-s1">joblib</span></div>
<div id="LC4" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div ">
</div>
<div id="LC5" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div "><span class="pl-c"># Load model dan scaler</span></div>
<div id="LC6" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div "><span class="pl-s1">model</span> <span class="pl-c1">=</span> <span class="pl-s1">joblib</span>.<span class="pl-c1">load</span>(<span class="pl-s">"model_obesitas.pkl"</span>)</div>
<div id="LC7" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div "><span class="pl-s1">scaler</span> <span class="pl-c1">=</span> <span class="pl-s1">joblib</span>.<span class="pl-c1">load</span>(<span class="pl-s">"scaler.pkl"</span>)</div>
<div id="LC8" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div ">
</div>
<div id="LC9" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div "><span class="pl-c"># Judul Aplikasi</span></div>
<div id="LC10" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div "><span class="pl-s1">st</span>.<span class="pl-c1">title</span>(<span class="pl-s">"Prediksi Tingkat Obesitas"</span>)</div>
<div id="LC11" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div "><span class="pl-s1">st</span>.<span class="pl-c1">markdown</span>(<span class="pl-s">"Masukkan data berikut untuk memprediksi tingkat obesitas:"</span>)</div>
<div id="LC12" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div ">
</div>
<div id="LC13" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div "><span class="pl-c"># Input data</span></div>
<div id="LC14" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div "><span class="pl-s1">age</span> <span class="pl-c1">=</span> <span class="pl-s1">st</span>.<span class="pl-c1">number_input</span>(<span class="pl-s">"Usia"</span>, <span class="pl-c1">10</span>, <span class="pl-c1">100</span>, <span class="pl-c1">25</span>)</div>
<div id="LC15" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div "><span class="pl-s1">height</span> <span class="pl-c1">=</span> <span class="pl-s1">st</span>.<span class="pl-c1">number_input</span>(<span class="pl-s">"Tinggi Badan (meter)"</span>, <span class="pl-c1">1.0</span>, <span class="pl-c1">2.5</span>, <span class="pl-c1">1.70</span>)</div>
<div id="LC16" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div "><span class="pl-s1">weight</span> <span class="pl-c1">=</span> <span class="pl-s1">st</span>.<span class="pl-c1">number_input</span>(<span class="pl-s">"Berat Badan (kg)"</span>, <span class="pl-c1">30</span>, <span class="pl-c1">200</span>, <span class="pl-c1">70</span>)</div>
<div id="LC17" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div "><span class="pl-s1">fcvc</span> <span class="pl-c1">=</span> <span class="pl-s1">st</span>.<span class="pl-c1">slider</span>(<span class="pl-s">"Konsumsi Sayur (FCVC)"</span>, <span class="pl-c1">1</span>, <span class="pl-c1">3</span>, <span class="pl-c1">2</span>)</div>
<div id="LC18" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div "><span class="pl-s1">ncp</span> <span class="pl-c1">=</span> <span class="pl-s1">st</span>.<span class="pl-c1">slider</span>(<span class="pl-s">"Jumlah Makan per Hari (NCP)"</span>, <span class="pl-c1">1</span>, <span class="pl-c1">4</span>, <span class="pl-c1">3</span>)</div>
<div id="LC19" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div "><span class="pl-s1">ch2o</span> <span class="pl-c1">=</span> <span class="pl-s1">st</span>.<span class="pl-c1">slider</span>(<span class="pl-s">"Minum Air (CH2O)"</span>, <span class="pl-c1">1</span>, <span class="pl-c1">3</span>, <span class="pl-c1">2</span>)</div>
<div id="LC20" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div "><span class="pl-s1">faf</span> <span class="pl-c1">=</span> <span class="pl-s1">st</span>.<span class="pl-c1">slider</span>(<span class="pl-s">"Aktivitas Fisik (FAF)"</span>, <span class="pl-c1">0</span>, <span class="pl-c1">3</span>, <span class="pl-c1">1</span>)</div>
<div id="LC21" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div "><span class="pl-s1">tue</span> <span class="pl-c1">=</span> <span class="pl-s1">st</span>.<span class="pl-c1">slider</span>(<span class="pl-s">"Waktu Pakai Teknologi (TUE)"</span>, <span class="pl-c1">0</span>, <span class="pl-c1">3</span>, <span class="pl-c1">1</span>)</div>
<div id="LC22" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div ">
</div>
<div id="LC23" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div "><span class="pl-c"># Fitur kategorikal</span></div>
<div id="LC24" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div "><span class="pl-s1">gender</span> <span class="pl-c1">=</span> <span class="pl-s1">st</span>.<span class="pl-c1">selectbox</span>(<span class="pl-s">"Jenis Kelamin"</span>, [<span class="pl-s">"Male"</span>, <span class="pl-s">"Female"</span>])</div>
<div id="LC25" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div "><span class="pl-s1">family_history</span> <span class="pl-c1">=</span> <span class="pl-s1">st</span>.<span class="pl-c1">selectbox</span>(<span class="pl-s">"Riwayat Keluarga Obesitas"</span>, [<span class="pl-s">"Yes"</span>, <span class="pl-s">"No"</span>])</div>
<div id="LC26" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div "><span class="pl-s1">favc</span> <span class="pl-c1">=</span> <span class="pl-s1">st</span>.<span class="pl-c1">selectbox</span>(<span class="pl-s">"Sering Konsumsi Makanan Tinggi Kalori?"</span>, [<span class="pl-s">"Yes"</span>, <span class="pl-s">"No"</span>])</div>
<div id="LC27" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div "><span class="pl-s1">caec</span> <span class="pl-c1">=</span> <span class="pl-s1">st</span>.<span class="pl-c1">selectbox</span>(<span class="pl-s">"Konsumsi Camilan?"</span>, [<span class="pl-s">"No"</span>, <span class="pl-s">"Sometimes"</span>, <span class="pl-s">"Frequently"</span>, <span class="pl-s">"Always"</span>])</div>
<div id="LC28" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div "><span class="pl-s1">smoke</span> <span class="pl-c1">=</span> <span class="pl-s1">st</span>.<span class="pl-c1">selectbox</span>(<span class="pl-s">"Merokok?"</span>, [<span class="pl-s">"Yes"</span>, <span class="pl-s">"No"</span>])</div>
<div id="LC29" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div "><span class="pl-s1">scc</span> <span class="pl-c1">=</span> <span class="pl-s1">st</span>.<span class="pl-c1">selectbox</span>(<span class="pl-s">"Kendalikan Kalori?"</span>, [<span class="pl-s">"Yes"</span>, <span class="pl-s">"No"</span>])</div>
<div id="LC30" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div "><span class="pl-s1">calc</span> <span class="pl-c1">=</span> <span class="pl-s1">st</span>.<span class="pl-c1">selectbox</span>(<span class="pl-s">"Konsumsi Alkohol?"</span>, [<span class="pl-s">"No"</span>, <span class="pl-s">"Sometimes"</span>, <span class="pl-s">"Frequently"</span>])</div>
<div id="LC31" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div "><span class="pl-s1">mtrans</span> <span class="pl-c1">=</span> <span class="pl-s1">st</span>.<span class="pl-c1">selectbox</span>(<span class="pl-s">"Transportasi"</span>, [<span class="pl-s">"Public_Transportation"</span>, <span class="pl-s">"Walking"</span>, <span class="pl-s">"Automobile"</span>, <span class="pl-s">"Motorbike"</span>, <span class="pl-s">"Bike"</span>])</div>
<div id="LC32" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div ">
</div>
<div id="LC33" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div "><span class="pl-c"># Encode kategorikal manual (harus sama dengan label encoder kamu saat training)</span></div>
<div id="LC34" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div "><span class="pl-k">def</span> <span class="pl-en">encode</span>(<span class="pl-s1">val</span>, <span class="pl-s1">mapping</span>):</div>
<div id="LC35" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div ">    <span class="pl-k">return</span> <span class="pl-s1">mapping</span>.<span class="pl-c1">get</span>(<span class="pl-s1">val</span>, <span class="pl-c1">0</span>)</div>
<div id="LC36" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div ">
</div>
<div id="LC37" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div "><span class="pl-s1">gender_map</span> <span class="pl-c1">=</span> {<span class="pl-s">"Male"</span>: <span class="pl-c1">1</span>, <span class="pl-s">"Female"</span>: <span class="pl-c1">0</span>}</div>
<div id="LC38" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div "><span class="pl-s1">family_map</span> <span class="pl-c1">=</span> {<span class="pl-s">"Yes"</span>: <span class="pl-c1">1</span>, <span class="pl-s">"No"</span>: <span class="pl-c1">0</span>}</div>
<div id="LC39" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div "><span class="pl-s1">favc_map</span> <span class="pl-c1">=</span> {<span class="pl-s">"Yes"</span>: <span class="pl-c1">1</span>, <span class="pl-s">"No"</span>: <span class="pl-c1">0</span>}</div>
<div id="LC40" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div "><span class="pl-s1">caec_map</span> <span class="pl-c1">=</span> {<span class="pl-s">"No"</span>: <span class="pl-c1">0</span>, <span class="pl-s">"Sometimes"</span>: <span class="pl-c1">1</span>, <span class="pl-s">"Frequently"</span>: <span class="pl-c1">2</span>, <span class="pl-s">"Always"</span>: <span class="pl-c1">3</span>}</div>
<div id="LC41" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div "><span class="pl-s1">smoke_map</span> <span class="pl-c1">=</span> {<span class="pl-s">"Yes"</span>: <span class="pl-c1">1</span>, <span class="pl-s">"No"</span>: <span class="pl-c1">0</span>}</div>
<div id="LC42" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div "><span class="pl-s1">scc_map</span> <span class="pl-c1">=</span> {<span class="pl-s">"Yes"</span>: <span class="pl-c1">1</span>, <span class="pl-s">"No"</span>: <span class="pl-c1">0</span>}</div>
<div id="LC43" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div "><span class="pl-s1">calc_map</span> <span class="pl-c1">=</span> {<span class="pl-s">"No"</span>: <span class="pl-c1">0</span>, <span class="pl-s">"Sometimes"</span>: <span class="pl-c1">1</span>, <span class="pl-s">"Frequently"</span>: <span class="pl-c1">2</span>}</div>
<div id="LC44" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div "><span class="pl-s1">mtrans_map</span> <span class="pl-c1">=</span> {<span class="pl-s">"Public_Transportation"</span>: <span class="pl-c1">0</span>, <span class="pl-s">"Walking"</span>: <span class="pl-c1">1</span>, <span class="pl-s">"Automobile"</span>: <span class="pl-c1">2</span>, <span class="pl-s">"Motorbike"</span>: <span class="pl-c1">3</span>, <span class="pl-s">"Bike"</span>: <span class="pl-c1">4</span>}</div>
<div id="LC45" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div ">
</div>
<div id="LC46" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div "><span class="pl-c"># Gabungkan input</span></div>
<div id="LC47" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div "><span class="pl-s1">data</span> <span class="pl-c1">=</span> <span class="pl-s1">np</span>.<span class="pl-c1">array</span>([[</div>
<div id="LC48" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div child-of-line-46 ">    <span class="pl-s1">age</span>,</div>
<div id="LC49" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div child-of-line-46 ">    <span class="pl-s1">height</span>,</div>
<div id="LC50" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div child-of-line-46 ">    <span class="pl-s1">weight</span>,</div>
<div id="LC51" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div child-of-line-46 ">    <span class="pl-s1">fcvc</span>,</div>
<div id="LC52" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div child-of-line-46 ">    <span class="pl-s1">ncp</span>,</div>
<div id="LC53" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div child-of-line-46 ">    <span class="pl-s1">ch2o</span>,</div>
<div id="LC54" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div child-of-line-46 ">    <span class="pl-s1">faf</span>,</div>
<div id="LC55" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div child-of-line-46 ">    <span class="pl-s1">tue</span>,</div>
<div id="LC56" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div child-of-line-46 ">    <span class="pl-en">encode</span>(<span class="pl-s1">gender</span>, <span class="pl-s1">gender_map</span>),</div>
<div id="LC57" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div child-of-line-46 ">    <span class="pl-en">encode</span>(<span class="pl-s1">family_history</span>, <span class="pl-s1">family_map</span>),</div>
<div id="LC58" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div child-of-line-46 ">    <span class="pl-en">encode</span>(<span class="pl-s1">favc</span>, <span class="pl-s1">favc_map</span>),</div>
<div id="LC59" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div child-of-line-46 ">    <span class="pl-en">encode</span>(<span class="pl-s1">caec</span>, <span class="pl-s1">caec_map</span>),</div>
<div id="LC60" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div child-of-line-46 ">    <span class="pl-en">encode</span>(<span class="pl-s1">smoke</span>, <span class="pl-s1">smoke_map</span>),</div></div>
<div class="react-no-virtualization-wrapper"><div id="LC61" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div child-of-line-46 ">    <span class="pl-en">encode</span>(<span class="pl-s1">scc</span>, <span class="pl-s1">scc_map</span>),</div>
<div id="LC62" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div child-of-line-46 ">    <span class="pl-en">encode</span>(<span class="pl-s1">calc</span>, <span class="pl-s1">calc_map</span>),</div>
<div id="LC63" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div child-of-line-46 ">    <span class="pl-en">encode</span>(<span class="pl-s1">mtrans</span>, <span class="pl-s1">mtrans_map</span>)</div>
<div id="LC64" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div ">]])</div>
<div id="LC65" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div ">
</div>
<div id="LC66" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div "><span class="pl-c"># Tombol prediksi</span></div>
<div id="LC67" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div "><span class="pl-k">if</span> <span class="pl-s1">st</span>.<span class="pl-c1">button</span>(<span class="pl-s">"Prediksi"</span>):</div>
<div id="LC68" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div ">    <span class="pl-s1">data_scaled</span> <span class="pl-c1">=</span> <span class="pl-s1">scaler</span>.<span class="pl-c1">transform</span>(<span class="pl-s1">data</span>)</div>
<div id="LC69" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div ">    <span class="pl-s1">pred</span> <span class="pl-c1">=</span> <span class="pl-s1">model</span>.<span class="pl-c1">predict</span>(<span class="pl-s1">data_scaled</span>)[<span class="pl-c1">0</span>]</div>
<div id="LC70" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div ">    </div>
<div id="LC71" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div ">    <span class="pl-s1">klasifikasi</span> <span class="pl-c1">=</span> {</div>
<div id="LC72" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div ">        <span class="pl-c1">0</span>: <span class="pl-s">"Berat Badan Kurang"</span>,</div>
<div id="LC73" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div ">        <span class="pl-c1">1</span>: <span class="pl-s">"Berat Badan Normal"</span>,</div>
<div id="LC74" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div ">        <span class="pl-c1">2</span>: <span class="pl-s">"Kelebihan Berat Badan Tingkat I"</span>,</div>
<div id="LC75" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div ">        <span class="pl-c1">3</span>: <span class="pl-s">"Kelebihan Berat Badan Tingkat II"</span>,</div>
<div id="LC76" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div ">        <span class="pl-c1">4</span>: <span class="pl-s">"Obesitas Tipe I"</span>,</div>
<div id="LC77" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div ">        <span class="pl-c1">5</span>: <span class="pl-s">"Obesitas Tipe II"</span>,</div>
<div id="LC78" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div ">        <span class="pl-c1">6</span>: <span class="pl-s">"Obesitas Tipe III"</span></div>
<div id="LC79" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div ">    }</div>
<div id="LC80" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div ">    <span class="pl-s1">st</span>.<span class="pl-c1">success</span>(<span class="pl-s">f"Hasil Prediksi: **<span class="pl-s1"><span class="pl-kos">{</span><span class="pl-s1">klasifikasi</span>[<span class="pl-s1">pred</span>]<span class="pl-kos">}</span></span>**"</span>)</div></div></div><div class="Box-sc-g0xbh4-0 jWasvN symbol-highlight react-code-text" data-testid="sticky-line-observer"></div></div><button hidden="" data-hotkey="Control+a"></button></div></div></div></div><div id="copilot-button-container"></div></div><div id="highlighted-line-menu-container"></div></div></div></section></div></div></div> <!-- --> <!-- --> </div></div></div></div></div></div></div><div id="find-result-marks-container" class="Box-sc-g0xbh4-0 cCoXib"></div><button hidden="" data-testid="" data-hotkey-scope="read-only-cursor-text-area" data-hotkey="Control+F6,Control+Shift+F6"></button><button hidden="" data-hotkey="Control+F6,Control+Shift+F6"></button></div> <!-- --> <!-- --> <script type="application/json" id="__PRIMER_DATA_:R0:__">{"resolvedServerColorMode":"night"}</script></div>
</react-app>




  </div>

</turbo-frame>

    </main>
  </div>

  </div>

          <footer class="footer pt-8 pb-6 f6 color-fg-muted p-responsive" role="contentinfo" hidden="">
  <h2 class="sr-only">Footer</h2>

  


  <div class="d-flex flex-justify-center flex-items-center flex-column-reverse flex-lg-row flex-wrap flex-lg-nowrap">
    <div class="d-flex flex-items-center flex-shrink-0 mx-2">
      <a aria-label="GitHub Homepage" class="footer-octicon mr-2" href="https://github.com/">
        <svg aria-hidden="true" height="24" viewBox="0 0 24 24" version="1.1" width="24" data-view-component="true" class="octicon octicon-mark-github">
    <path d="M12 1C5.9225 1 1 5.9225 1 12C1 16.8675 4.14875 20.9787 8.52125 22.4362C9.07125 22.5325 9.2775 22.2025 9.2775 21.9137C9.2775 21.6525 9.26375 20.7862 9.26375 19.865C6.5 20.3737 5.785 19.1912 5.565 18.5725C5.44125 18.2562 4.905 17.28 4.4375 17.0187C4.0525 16.8125 3.5025 16.3037 4.42375 16.29C5.29 16.2762 5.90875 17.0875 6.115 17.4175C7.105 19.0812 8.68625 18.6137 9.31875 18.325C9.415 17.61 9.70375 17.1287 10.02 16.8537C7.5725 16.5787 5.015 15.63 5.015 11.4225C5.015 10.2262 5.44125 9.23625 6.1425 8.46625C6.0325 8.19125 5.6475 7.06375 6.2525 5.55125C6.2525 5.55125 7.17375 5.2625 9.2775 6.67875C10.1575 6.43125 11.0925 6.3075 12.0275 6.3075C12.9625 6.3075 13.8975 6.43125 14.7775 6.67875C16.8813 5.24875 17.8025 5.55125 17.8025 5.55125C18.4075 7.06375 18.0225 8.19125 17.9125 8.46625C18.6138 9.23625 19.04 10.2125 19.04 11.4225C19.04 15.6437 16.4688 16.5787 14.0213 16.8537C14.42 17.1975 14.7638 17.8575 14.7638 18.8887C14.7638 20.36 14.75 21.5425 14.75 21.9137C14.75 22.2025 14.9563 22.5462 15.5063 22.4362C19.8513 20.9787 23 16.8537 23 12C23 5.9225 18.0775 1 12 1Z"></path>
</svg>
</a>
      <span>
        © 2025 GitHub,&nbsp;Inc.
      </span>
    </div>

    <nav aria-label="Footer">
      <h3 class="sr-only" id="sr-footer-heading">Footer navigation</h3>

      <ul class="list-style-none d-flex flex-justify-center flex-wrap mb-2 mb-lg-0" aria-labelledby="sr-footer-heading">

          <li class="mx-2">
            <a data-analytics-event="{&quot;category&quot;:&quot;Footer&quot;,&quot;action&quot;:&quot;go to Terms&quot;,&quot;label&quot;:&quot;text:terms&quot;}" href="https://docs.github.com/site-policy/github-terms/github-terms-of-service" data-view-component="true" class="Link--secondary Link">Terms</a>
          </li>

          <li class="mx-2">
            <a data-analytics-event="{&quot;category&quot;:&quot;Footer&quot;,&quot;action&quot;:&quot;go to privacy&quot;,&quot;label&quot;:&quot;text:privacy&quot;}" href="https://docs.github.com/site-policy/privacy-policies/github-privacy-statement" data-view-component="true" class="Link--secondary Link">Privacy</a>
          </li>

          <li class="mx-2">
            <a data-analytics-event="{&quot;category&quot;:&quot;Footer&quot;,&quot;action&quot;:&quot;go to security&quot;,&quot;label&quot;:&quot;text:security&quot;}" href="https://github.com/security" data-view-component="true" class="Link--secondary Link">Security</a>
          </li>

          <li class="mx-2">
            <a data-analytics-event="{&quot;category&quot;:&quot;Footer&quot;,&quot;action&quot;:&quot;go to status&quot;,&quot;label&quot;:&quot;text:status&quot;}" href="https://www.githubstatus.com/" data-view-component="true" class="Link--secondary Link">Status</a>
          </li>

          <li class="mx-2">
            <a data-analytics-event="{&quot;category&quot;:&quot;Footer&quot;,&quot;action&quot;:&quot;go to docs&quot;,&quot;label&quot;:&quot;text:docs&quot;}" href="https://docs.github.com/" data-view-component="true" class="Link--secondary Link">Docs</a>
          </li>

          <li class="mx-2">
            <a data-analytics-event="{&quot;category&quot;:&quot;Footer&quot;,&quot;action&quot;:&quot;go to contact&quot;,&quot;label&quot;:&quot;text:contact&quot;}" href="https://support.github.com/?tags=dotcom-footer" data-view-component="true" class="Link--secondary Link">Contact</a>
          </li>

          <li class="mx-2">
  <cookie-consent-link data-catalyst="">
    <button type="button" class="Link--secondary underline-on-hover border-0 p-0 color-bg-transparent" data-action="click:cookie-consent-link#showConsentManagement" data-analytics-event="{&quot;location&quot;:&quot;footer&quot;,&quot;action&quot;:&quot;cookies&quot;,&quot;context&quot;:&quot;subfooter&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;label&quot;:&quot;cookies_link_subfooter_footer&quot;}">
       Manage cookies
    </button>
  </cookie-consent-link>
</li>

<li class="mx-2">
  <cookie-consent-link data-catalyst="">
    <button type="button" class="Link--secondary underline-on-hover border-0 p-0 color-bg-transparent" data-action="click:cookie-consent-link#showConsentManagement" data-analytics-event="{&quot;location&quot;:&quot;footer&quot;,&quot;action&quot;:&quot;dont_share_info&quot;,&quot;context&quot;:&quot;subfooter&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;label&quot;:&quot;dont_share_info_link_subfooter_footer&quot;}">
      Do not share my personal information
    </button>
  </cookie-consent-link>
</li>

      </ul>
    </nav>
  </div>
</footer>



    <ghcc-consent id="ghcc" class="position-fixed bottom-0 left-0" style="z-index: 999999" data-locale="en" data-initial-cookie-consent-allowed="" data-cookie-consent-required="false" data-catalyst=""></ghcc-consent>



  <div id="ajax-error-message" class="ajax-error-message flash flash-error" hidden="">
    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-alert">
    <path d="M6.457 1.047c.659-1.234 2.427-1.234 3.086 0l6.082 11.378A1.75 1.75 0 0 1 14.082 15H1.918a1.75 1.75 0 0 1-1.543-2.575Zm1.763.707a.25.25 0 0 0-.44 0L1.698 13.132a.25.25 0 0 0 .22.368h12.164a.25.25 0 0 0 .22-.368Zm.53 3.996v2.5a.75.75 0 0 1-1.5 0v-2.5a.75.75 0 0 1 1.5 0ZM9 11a1 1 0 1 1-2 0 1 1 0 0 1 2 0Z"></path>
</svg>
    <button type="button" class="flash-close js-ajax-error-dismiss" aria-label="Dismiss error">
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-x">
    <path d="M3.72 3.72a.75.75 0 0 1 1.06 0L8 6.94l3.22-3.22a.749.749 0 0 1 1.275.326.749.749 0 0 1-.215.734L9.06 8l3.22 3.22a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215L8 9.06l-3.22 3.22a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042L6.94 8 3.72 4.78a.75.75 0 0 1 0-1.06Z"></path>
</svg>
    </button>
    You can’t perform that action at this time.
  </div>

    <template id="site-details-dialog"></template>

    <div class="Popover js-hovercard-content position-absolute" style="display: none; outline: none;">
  <div class="Popover-message Popover-message--bottom-left Popover-message--large Box color-shadow-large" style="width:360px;"></div>
</div>

    <template id="snippet-clipboard-copy-button"></template>
<template id="snippet-clipboard-copy-button-unpositioned"></template>


    <style>
      .user-mention[href$="/Jetgar"] {
        color: var(--color-user-mention-fg);
        background-color: var(--bgColor-attention-muted, var(--color-attention-subtle));
        border-radius: 2px;
        margin-left: -2px;
        margin-right: -2px;
      }
      .user-mention[href$="/Jetgar"]:before,
      .user-mention[href$="/Jetgar"]:after {
        content: '';
        display: inline-block;
        width: 2px;
      }
    </style>


    </div>

    <div id="js-global-screen-reader-notice" class="sr-only mt-n1" aria-live="polite" aria-atomic="true">-Deploy_ke_Streamlit_Cloud/app.py at main · fastabyq/-Deploy_ke_Streamlit_Cloud</div>
    <div id="js-global-screen-reader-notice-assertive" class="sr-only mt-n1" aria-live="assertive" aria-atomic="true"></div>
  


<div class="sr-only mt-n1" id="screenReaderAnnouncementDiv" role="alert" data-testid="screenReaderAnnouncement" aria-live="assertive">&nbsp;</div></body></html>